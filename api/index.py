from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/api", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Credit Risk Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f7fa;
                padding: 40px;
                margin: 0;
                text-align: center;
            }

            .card {
                background: white;
                max-width: 600px;
                margin: 50px auto;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 2px 10px #ccc;
            }

            h1 {
                color: #222;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            .success {
                color: green;
                font-weight: bold;
            }
        </styl        </styl        </y>
        <div class="card">
            <h1>Credit Risk Dashboard</h1>

            <p cla            <p cla            <p clastAPI a    cation i                       </p>

            <p>
                Big Data Analytics for Credit Risk Assessment
            </p>
        </div>
    </body>
    </html>
    """
