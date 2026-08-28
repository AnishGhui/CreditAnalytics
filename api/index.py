```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
import os

app = FastAPI()

DATA_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "raw_data.csv"
)


@app.get("/", response_class=HTMLResponse)
def home():
    df = pd.read_csv(DATA_PATH)

    # Find the default/payment-default column
    target = next(
        col for col in df.columns
        if "default" in col.lower()
    )

    customers = len(df)
    default_rate = df[target].mean() * 100
    avg_credit = df["LIMIT_BAL"].mean()
    avg_age = df["AGE"].mean()
    default_customers = (df[target] == 1).sum()
    non_default_customers = (df[target] == 0).sum()

    return f"""
    <html>
    <head>
        <title>Credit Risk Dashboard</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f5f7fa;
                padding: 40px;
            }}

            h1 {{
                color: #222;
            }}

            .cards {{
                display: flex;
                gap: 20px;
                flex-wrap: wrap;
            }}

            .card {{
                background: white;
                padding: 25px;
                border-radius: 10px;
                width: 200px;
                box-shadow: 0 2px 8px #ccc;
            }}

            .value {{
                font-size: 28px;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>

        <h1>Credit Risk Dashboard</h1>

        <p>Big Data Analytics for Credit Risk Assessment</p>

        <div class="cards">

            <div class="card">
                <h3>👥 Customers</h3>
                <div class="value">{customers:,}</div>
            </div>

            <div class="card">
                <h3>⚠️ Default Rate</h3>
                <div class="value">{default_rate:.2f}%</div>
            </div>

            <div class="card">
                <h3>💰 Average Credit</h3>
                <div class="value">${avg_credit:,.0f}</div>
            </div>

            <div class="card">
                <h3>🎂 Average Age</h3>
                <div class="value">{avg_age:.1f}</div>
            </div>

        </div>

        <h2>Risk Analysis</h2>

        <p>
            Default customers:
            <strong>{default_customers:,}</strong>
        </p>

        <p>
            Non-default customers:
            <strong>{non_default_customers:,}</strong>
        </p>

    </body>
    </html>
    """

