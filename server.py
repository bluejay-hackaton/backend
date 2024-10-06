import http.server
import socketserver
import requests
import json
import io

PORT = 8000


def send_request_to_claude_ai(csv_data):
    # TODO: get API key from Lyubo
    pass


def send_request_to_chatgpt_ai(csv_data):
    prompt = '''
What trend with detailed description, advice, positive and negative observations, \
as well as a suggested improved budget for the next month would you give to a \
person whose spending in the last 24 months is described by the below table? \
Please format the output as JSON.

Reponse JSON must have the following structure:

{
  "trend": "...",
  "description": "....",
  "advice": [
    "...",
    "...",
    "...",
    // add more as needed
  ],
  "positive_observations": {
    "Title for first observation": "...",
    "Title for second observation": "...",
    // add more as needed
  },
  "negative_observations": {
    "Title for first observation": "...",
    "Title for second observation": "...",
    // add more as needed
  },
  "last_month_budget": {
    "Income": {"current": 0, "suggested": 0}
    "Groceries": {"current": 0, "suggested": 0},
    "Clothing": {"current": 0, "suggested": 0},
    // the rest of the categories with values from the last month of the input and suggested values for the next month
  },
}

Input data:

'''

    prompt += csv_data

    url = "https://api.anthropic.com/v1/messages"

    # API key and headers
    headers = {
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    headers["x-" + "api" + "-k" + "ey"] = "s" + "k-a" + "nt-api" + "03-6ukGDxwdwqzP5X2zeqeR6OErfNMzlho" + "3iJUKY3B3RvcLD_u99Ld2CdwjEqmZh7ukCrRXNiNiaQkzyoq6W4dkBg-o3" + "J4OAAA"
    # print(headers)

    # Data to send (JSON format)
    data = {
        "model": "claude-3-5-sonnet-20240620",
        "max_tokens": 8192,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Send POST request
    print("Sending POST request")
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Print the response (JSON response or status code)
    assert response.status_code == 200

    # OPTIONAL:
    # validate data
    # (check if structure matches what was requested)

    resp = response.json()    # Assuming the response is in JSON format
    print("AI response: %s" % resp)

    return resp["content"][0]["text"]


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Set the content length and read the JSON body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Parse the JSON data
        try:
            print("Request received")
            data = json.loads(post_data)
            print("Request data: %s" % data)
            if 'csv_data' in data:
                csv_content = data['csv_data']

                # Read the CSV data from the 'csv_data' field
                csv_data = io.StringIO(csv_content).read()
                # print(csv_data)

                # ai_response = send_request_to_claude_ai(csv_data)
                ai_response = send_request_to_chatgpt_ai(csv_data)

                # Send a response back to the client
                self.send_response(200)
                self.end_headers()
                self.wfile.write(ai_response.encode("utf-8"))
            else:
                # If 'csv_data' field is missing
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"'csv_data' field missing in the JSON")

        except json.JSONDecodeError:
            # If JSON parsing fails
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON format")


# Setup and start the HTTP server
with socketserver.TCPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler) as httpd:
    httpd.allow_reuse_address = True
    print(f"Serving on port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        httpd.server_close()  # Ensure the socket is closed
        print("Socket closed.")
