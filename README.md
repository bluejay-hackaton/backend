### Quick start

Install dependencies

```
pip install -r requirements.txt
```

Start the server (port 8000):

```
python server.py
```

Send an example request:

curl -X POST http://127.0.0.1:8000 --data-binary @example.json

Example response (plain text):

```
{
  "trend": "Increasing discretionary spending and debt, decreasing savings",
  "description": "Over the past 24 months, there's been a significant increase in spending on non-essential categories like entertainment, dining, and clothing. Simultaneously, investment savings have disappeared, and high-interest loan repayments have more than quadrupled. While income has increased by 12%, expenses in many categories have grown at a much faster rate.",
  "advice": [
    "Immediately reduce spending on entertainment and dining out",
    "Reinstate investment savings, even if starting small",
    "Focus on paying down high-interest debt more aggressively",
    "Consider seeking additional income sources or a higher-paying job to match increased expenses",
    "Re-evaluate the need for increased spending on clothing and personal items"
  ],
  "positive_observations": {
    "Income Growth": "Gross income has increased from $5000 to $5600 over two years, showing career progression.",
    "Consistent Essential Payments": "Housing, utilities, and low-interest loan payments have remained stable, indicating good management of fixed costs."
  },
  "negative_observations": {
    "Elimination of Savings": "Investment savings have dropped from $300 to $0, jeopardizing long-term financial health.",
    "Ballooning High-Interest Debt": "High-interest loan repayments have increased from $200 to $850, indicating accumulating debt.",
    "Excessive Discretionary Spending": "Entertainment and dining expenses have more than tripled, from $500 to $1420 combined.",
    "Neglect of Personal Development": "Spending on education and wellness has been completely cut, potentially impacting future earning potential and health."
  },
  "last_month_budget": {
    "Income": {"avg_last_6_months": 5600, "current": 5600, "suggested": 5600},
    "Groceries": {"avg_last_6_months": 705, "current": 730, "suggested": 650},
    "Clothing": {"avg_last_6_months": 275, "current": 300, "suggested": 150},
    "Utilities": {"avg_last_6_months": 330, "current": 330, "suggested": 330},
    "Entertainment": {"avg_last_6_months": 610, "current": 660, "suggested": 300},
    "Dining": {"avg_last_6_months": 707, "current": 760, "suggested": 400},
    "Transport": {"avg_last_6_months": 180, "current": 180, "suggested": 180},
    "Insurance": {"avg_last_6_months": 200, "current": 200, "suggested": 200},
    "Medical expenses": {"avg_last_6_months": 283, "current": 320, "suggested": 320},
    "Housing": {"avg_last_6_months": 1500, "current": 1500, "suggested": 1500},
    "Investment savings": {"avg_last_6_months": 0, "current": 0, "suggested": 300},
    "Loan repayments (high interest)": {"avg_last_6_months": 725, "current": 850, "suggested": 1000},
    "Loan repayments (low interest)": {"avg_last_6_months": 400, "current": 400, "suggested": 400},
    "Charity": {"avg_last_6_months": 50, "current": 50, "suggested": 50},
    "Vacation": {"avg_last_6_months": 0, "current": 0, "suggested": 0},
    "Education": {"avg_last_6_months": 0, "current": 0, "suggested": 50},
    "Wellness": {"avg_last_6_months": 0, "current": 0, "suggested": 50},
    "Car maintenance": {"avg_last_6_months": 267, "current": 320, "suggested": 220}
  }
}
```
