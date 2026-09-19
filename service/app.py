from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI CI/CD Demo")


# -------------------------
# Home Page
# -------------------------
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>FastAPI CI/CD Demo</title>

        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                min-height: 100vh;
                font-family:
                    "Segoe UI",
                    Tahoma,
                    Geneva,
                    Verdana,
                    sans-serif;

                background:
                    linear-gradient(
                        135deg,
                        #0f172a 0%,
                        #1e293b 45%,
                        #2563eb 100%
                    );

                display: flex;
                justify-content: center;
                align-items: center;

                color: #ffffff;
                padding: 20px;
            }

            .container {
                width: 100%;
                max-width: 650px;
            }

            .card {
                background: rgba(255, 255, 255, 0.10);

                border: 1px solid rgba(255, 255, 255, 0.18);

                border-radius: 20px;

                padding: 45px;

                text-align: center;

                backdrop-filter: blur(14px);

                box-shadow:
                    0 25px 60px rgba(0, 0, 0, 0.35);
            }

            .icon {
                width: 70px;
                height: 70px;

                margin: 0 auto 22px;

                display: flex;
                align-items: center;
                justify-content: center;

                border-radius: 18px;

                background: rgba(255, 255, 255, 0.12);

                font-size: 34px;
            }

            h1 {
                font-size: 34px;
                margin-bottom: 12px;

                letter-spacing: -0.8px;
            }

            .subtitle {
                color: rgba(255, 255, 255, 0.78);

                font-size: 16px;

                line-height: 1.6;

                margin-bottom: 30px;
            }

            .status {
                display: inline-flex;

                align-items: center;

                gap: 8px;

                background: rgba(34, 197, 94, 0.15);

                border: 1px solid rgba(34, 197, 94, 0.35);

                color: #86efac;

                padding: 8px 14px;

                border-radius: 999px;

                font-size: 13px;

                font-weight: 600;

                margin-bottom: 30px;
            }

            .status-dot {
                width: 8px;
                height: 8px;

                background: #22c55e;

                border-radius: 50%;

                box-shadow: 0 0 10px #22c55e;
            }

            .endpoints {
                text-align: left;

                background: rgba(0, 0, 0, 0.18);

                border-radius: 14px;

                padding: 20px;

                margin-top: 10px;
            }

            .endpoints h3 {
                font-size: 15px;

                margin-bottom: 15px;

                color: rgba(255, 255, 255, 0.9);
            }

            .endpoint {
                display: flex;

                align-items: center;

                justify-content: space-between;

                padding: 12px 14px;

                margin-bottom: 8px;

                background: rgba(255, 255, 255, 0.07);

                border-radius: 9px;
            }

            .endpoint:last-child {
                margin-bottom: 0;
            }

            .method {
                color: #86efac;

                font-size: 11px;

                font-weight: 700;

                background: rgba(34, 197, 94, 0.12);

                padding: 5px 7px;

                border-radius: 5px;

                margin-right: 10px;
            }

            .endpoint-left {
                display: flex;

                align-items: center;
            }

            .path {
                font-family: monospace;

                font-size: 14px;

                color: #ffffff;
            }

            .description {
                color: rgba(255, 255, 255, 0.55);

                font-size: 12px;
            }

            .footer {
                margin-top: 28px;

                color: rgba(255, 255, 255, 0.5);

                font-size: 12px;
            }

            .tech {
                margin-top: 8px;

                color: rgba(255, 255, 255, 0.7);

                font-size: 13px;
            }

            @media (max-width: 600px) {
                .card {
                    padding: 30px 20px;
                }

                h1 {
                    font-size: 27px;
                }

                .endpoint {
                    align-items: flex-start;
                }

                .description {
                    display: none;
                }
            }
        </style>
    </head>

    <body>

        <div class="container">

            <div class="card">

                <div class="icon">
                    ⚡
                </div>

                <div class="status">
                    <span class="status-dot"></span>
                    Application Online
                </div>

                <h1>FastAPI CI/CD Demo</h1>

                <p class="subtitle">
                    A lightweight FastAPI application running inside
                    a container and ready for CI/CD and Kubernetes deployment.
                </p>


                <div class="endpoints">

                    <h3>Available Endpoints</h3>


                    <div class="endpoint">

                        <div class="endpoint-left">

                            <span class="method">
                                GET
                            </span>

                            <span class="path">
                                /
                            </span>

                        </div>

                        <span class="description">
                            Home
                        </span>

                    </div>


                    <div class="endpoint">

                        <div class="endpoint-left">

                            <span class="method">
                                GET
                            </span>

                            <span class="path">
                                /healthz
                            </span>

                        </div>

                        <span class="description">
                            Health Check
                        </span>

                    </div>

                </div>


                <div class="footer">
                    Built with ❤️ using FastAPI
                </div>

                <div class="tech">
                    Python • FastAPI • Docker • Kubernetes
                </div>

            </div>

        </div>

    </body>
    </html>
    """


# -------------------------
# Health Check
# -------------------------
@app.get("/healthz")
def health_check():
    return {
        "status": "healthy"
    }

