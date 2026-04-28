from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>DYPIU - AI Autoscaler</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family: Arial, sans-serif; background:#fff7f0; }

        .hero { background:linear-gradient(135deg,#FF6A00,#FF8C00,#FFA500);
                padding:60px 20px; text-align:center; color:white; }

        .badge { background:rgba(255,255,255,0.2); border:1px solid rgba(255,255,255,0.3);
                 border-radius:20px; padding:6px 20px; font-size:13px;
                 display:inline-block; margin-bottom:20px; letter-spacing:1px; }

        h1 { font-size:42px; margin-bottom:12px; }

        .divider { width:60px; height:3px; background:#FFD580;
                   margin:0 auto 20px; border-radius:2px; }

        h2 { font-size:22px; color:#FFE0B2; margin-bottom:12px; }

        .subtitle { color:rgba(255,255,255,0.8); font-size:14px; margin-bottom:32px; }

        .pills { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }

        .pill { background:rgba(255,255,255,0.2); border:1px solid rgba(255,255,255,0.3);
                border-radius:8px; padding:8px 20px; font-size:13px; }

        .stats { display:grid; grid-template-columns:repeat(4,1fr);
                 gap:16px; padding:24px; max-width:900px; margin:0 auto; }

        .stat { border-radius:12px; padding:20px; text-align:center; }

        .stat .num { font-size:32px; font-weight:700; }

        .stat .label { font-size:12px; margin-top:4px; }

        .flow { background:white; margin:0 24px 24px; border-radius:12px;
                padding:24px; text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.08); }

        .flow h3 { margin-bottom:20px; color:#333; }

        .flow-row { display:flex; align-items:center; justify-content:center;
                    flex-wrap:wrap; gap:8px; font-size:13px; }

        .flow-box { border-radius:8px; padding:10px 16px; font-weight:500; }

        .arrow { color:#FF8C00; font-size:20px; }

        .status { background:#FFF3E0; color:#E65100; border-radius:8px;
                  padding:12px 24px; display:inline-block;
                  margin:0 24px 24px; font-size:14px; }

    </style>
</head>
<body>

    <div class="hero">
        <div class="badge">D.Y. PATIL INTERNATIONAL UNIVERSITY</div>
        <h1>Welcome to DYPIU</h1>
        <div class="divider"></div>

        <h2>AI-Based Serverless Predictive<br>Auto-Scaler for Cloud Applications</h2>

        <p class="subtitle">Final Year Project — Computer Engineering 2025-26</p>

        <div class="pills">
            <span class="pill">Azure Functions</span>
            <span class="pill">Python AI</span>
            <span class="pill">Cloud Scaling</span>
        </div>
    </div>

    <div class="stats">
        <div class="stat" style="background:#FFF3E0;">
            <div class="num" style="color:#E65100;">5 min</div>
            <div class="label" style="color:#FF8C00;">Prediction interval</div>
        </div>

        <div class="stat" style="background:#FFE0B2;">
            <div class="num" style="color:#BF360C;">70%</div>
            <div class="label" style="color:#E65100;">CPU scale-out threshold</div>
        </div>

        <div class="stat" style="background:#FFF8E1;">
            <div class="num" style="color:#FF6F00;">AI</div>
            <div class="label" style="color:#FFA000;">Predictive engine</div>
        </div>

        <div class="stat" style="background:#FFFDE7;">
            <div class="num" style="color:#E65100;">24/7</div>
            <div class="label" style="color:#FF8F00;">Serverless monitoring</div>
        </div>
    </div>

    <div class="flow">
        <h3>How it works</h3>

        <div class="flow-row">
            <div class="flow-box" style="background:#FFF3E0;color:#E65100;">User traffic</div>
            <span class="arrow">→</span>

            <div class="flow-box" style="background:#FFF3E0;color:#E65100;">Web App</div>
            <span class="arrow">→</span>

            <div class="flow-box" style="background:#FFE0B2;color:#BF360C;">Azure Monitor</div>
            <span class="arrow">→</span>

            <div class="flow-box" style="background:#FFF8E1;color:#FF6F00;">AI Prediction</div>
            <span class="arrow">→</span>

            <div class="flow-box" style="background:#FFFDE7;color:#E65100;">Auto Scale</div>
        </div>
    </div>

    <div style="text-align:center;">
        <div class="status">Status: Running and being monitored</div>
    </div>

</body>
</html>
    '''

@app.route('/health')
def health():
    return {"status": "healthy", "app": "autoscaler-demo"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
