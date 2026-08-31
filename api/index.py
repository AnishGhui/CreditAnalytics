
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    customers = 30000
    default_rate = 22.12
    avg_credit = 167000
    avg_age = 35.5
    default_customers = 6636
    non_default_customers = customers - default_customers

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Credit Risk Dashboard</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                font-family: Arial, Helvetica, sans-serif;
                background: #f5f7fa;
                color: #222;
            }}

            .header {{
                background: #1f2937;
                color: white;
                padding: 30px 40px;
            }}

            .header h1 {{
                margin: 0 0 8px 0;
                font-size: 32px;
            }}

            .header p {{
                margin: 0;
                color: #d1d5db;
                font-size: 16px;
            }}

            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 35px 25px;
            }}

            .cards {{
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 20px;
                margin-bottom: 30px;
            }}

            .card {{
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            }}

            .card-title {{
                color: #6b7280;
                font-size: 14px;
                margin-bottom: 12px;
            }}

            .value {{
                font-size: 30px;
                font-weight: bold;
                color: #111827;
            }}

            .section {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
                margin-bottom: 25px;
            }}

            .section h2 {{
                margin-top: 0;
                color: #111827;
            }}

            .section p {{
                color: #4b5563;
                line-height: 1.6;
            }}

            .risk-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 20px;
                margin-top: 20px;
            }}

            .risk-box {{
                padding: 25px;
                border-radius: 10px;
                background: #f9fafb;
            }}

            .risk-box h3 {{
                margin-top: 0;
            }}

            .risk-number {{
                font-size: 28px;
                font-weight: bold;
                margin-top: 10px;
            }}

            .default {{
                border-left: 5px solid #dc2626;
            }}

            .non-default {{
                border-left: 5px solid #16a34a;
            }}

            .footer {{
                text-align: center;
                color: #6b7280;
                padding: 20px;
                font-size: 14px;
            }}

            @media (max-width: 800px) {{
                .cards {{
                    grid-template-columns: repeat(2, 1fr);
                }}

                .risk-grid {{
                    grid-template-columns: 1fr;
                }}
            }}

            @media (max-width: 500px) {{
                .cards {{
                    grid-template-columns: 1fr;
                }}

                .header {{
                    padding: 25px 20px;
                }}

                .container {{
                    padding: 25px 15px;
                }}
            }}
        </style>
    </head>

    <body>

        <div class="header">
            <h1>Credit Risk Dashboard</h1>
            <p>Big Data Analytics for Credit Risk Assessment</p>
        </div>

        <div class="container">

            <div class="cards">

                <div class="card">
                    <div class="card-title">👥 CUSTOMERS</div>
                    <div class="value">{customers:,}</div>
                </div>

                <div class="card">
                    <div class="card-title">⚠️ DEFAULT RATE</div>
                    <div class="value">{default_rate:.2f}%</div>
                </div>

                <div class="card">
                    <div class="card-title">💰 AVERAGE CREDIT</div>
                    <div class="value">${avg_credit:,.0f}</div>
                </div>

                <div class="card">
                    <div class="card-title">🎂 AVERAGE AGE</div>
                    <div class="value">{avg_age:.1f}</div>
                </div>

            </div>


            <div class="section">

                <h2>📊 Credit Risk Analysis</h2>

                <p>
                    This dashboard provides an overview of customer credit
                    information and default risk based on the credit card
                    customer dataset.
                </p>

                <div class="risk-grid">

                    <div class="risk-box default">
                        <h3>⚠️ Default Customers</h3>

                        <div class="risk-number">
                            {default_customers:,}
                        </div>

                        <p>
                            Customers identified as having defaulted
                            on their credit payments.
                        </p>
                    </div>


                    <div class="risk-box non-default">
                        <h3>✅ Non-Default Customers</h3>

                        <div class="risk-number">
                            {non_default_customers:,}
                        </div>

                        <p>
                            Customers who did not default on their
                            credit payments.
                        </p>
                    </div>

                </div>

            </div>


            <div class="section">

                <h2>🎯 Key Findings</h2>

                <p>
                    The dataset contains <strong>{customers:,}</strong>
                    customers. The overall default rate is
                    <strong>{default_rate:.2f}%</strong>.
                </p>

                <p>
                    The average credit limit is approximately
                    <strong>${avg_credit:,.0f}</strong>, while the
                    average customer age is
                    <strong>{avg_age:.1f} years</strong>.
                </p>

            </div>

        </div>

        <div class="footer">
            Credit Risk Analytics Dashboard • FastAPI
        </div>

    </body>
    </html>
    """
