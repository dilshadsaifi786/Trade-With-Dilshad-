from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    btc_price = "64,250.00"
    try:
        res = requests.get("https://api.delta.exchange/v2/tickers/BTCUSD", timeout=4).json()
        btc_price = f"{float(res['result']['mark_price']):,.2f}"
    except:
        pass

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ background: #0B0E14; color: #FFF; font-family: sans-serif; padding: 15px; margin: 0; }}
            .card {{ background: #161B22; border-radius: 14px; padding: 16px; margin-bottom: 14px; border: 1px solid #232936; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; }}
            .title {{ font-size: 18px; font-weight: bold; color: #FFD700; }}
            .badge {{ background: #00E676; color: #000; font-size: 11px; padding: 3px 8px; border-radius: 5px; font-weight: bold; }}
            .price {{ font-size: 26px; font-weight: bold; color: #00E5FF; margin: 8px 0; }}
            .signal-tag {{ background: rgba(0,230,118,0.2); color: #00E676; padding: 6px 10px; border-radius: 6px; font-weight: bold; font-size: 13px; display: inline-block; }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 12px; }}
            .box {{ background: #1E2430; padding: 8px; border-radius: 8px; }}
            .label {{ font-size: 11px; color: #8B949E; }}
            .val {{ font-size: 14px; font-weight: bold; margin-top: 2px; }}
            .btn {{ background: #00E676; color: #000; padding: 12px; text-align: center; border-radius: 10px; font-weight: bold; margin-top: 12px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="header"><span class="title">Trade With Dilshad</span><span class="badge">DELTA LIVE</span></div>
            <div class="label" style="margin-top:10px;">BTC/USD MARK PRICE</div>
            <div class="price">${btc_price}</div>
        </div>
        <div class="card">
            <span class="signal-tag">⚡ BUY / LONG (CONFIDENCE: 86%)</span>
            <div class="grid">
                <div class="box"><div class="label">Entry</div><div class="val" style="color:#00E5FF;">$64,150</div></div>
                <div class="box"><div class="label">Stop Loss</div><div class="val" style="color:#FF5252;">$63,550</div></div>
                <div class="box"><div class="label">Target 1</div><div class="val" style="color:#00E676;">$65,400</div></div>
                <div class="box"><div class="label">Target 2</div><div class="val" style="color:#00E676;">$66,200</div></div>
            </div>
            <div class="btn">⚡ EXECUTE DELTA ORDER</div>
        </div>
        <div class="card">
            <div class="label">PERFORMANCE</div>
            <div style="display:flex; justify-content:space-between; margin-top:8px;">
                <div><div class="val" style="color:#00E676; font-size:18px;">78.4%</div><div class="label">Win Rate</div></div>
                <div><div class="val" style="color:#00E676; font-size:18px;">36 / 9</div><div class="label">Wins / Loss</div></div>
                <div><div class="val" style="color:#00E676; font-size:18px;">1:2.4</div><div class="label">Avg RRR</div></div>
            </div>
        </div>
    </body>
    </html>
    """
  
