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
        body { font-family: Arial, sans-serif; background:#FFF7ED; }

        /* Hero Section */
        .hero {
            background: linear-gradient(135deg,#7C2D00 0%,#C2410C 40%,#EA580C 70%,#FB923C 100%);
            padding: 60px 20px;
            text-align: center;
            color: white;
            position: relative;
            overflow: hidden;
        }
        .hero::before {
            content:'';
            position:absolute; top:-40px; right:-40px;
            width:180px; height:180px;
            background:rgba(255,255,255,0.05);
            border-radius:50%;
        }
        .hero::after {
            content:'';
            position:absolute; bottom:-60px; left:-30px;
            width:220px; height:220px;
            background:rgba(255,255,255,0.04);
            border-radius:50%;
        }
        .badge {
            display:inline-block;
            background:rgba(255,255,255,0.18);
            border:1px solid rgba(255,255,255,0.35);
            border-radius:20px;
            padding:6px 22px;
            font-size:12px;
            color:#FED7AA;
            margin-bottom:20px;
            letter-spacing:1.5px;
            font-weight:500;
        }
        .cloud-icon {
            font-size:48px;
            margin-bottom:12px;
            display:block;
            animation: float 3s ease-in-out infinite;
        }
        h1 {
            font-size:42px;
            font-weight:800;
            color:#ffffff;
            margin:0 0 10px;
            text-shadow:0 2px 12px rgba(0,0,0,0.2);
        }
        .divider {
            width:70px; height:4px;
            background:#FED7AA;
            margin:0 auto 22px;
            border-radius:2px;
        }
        h2 {
            font-size:20px;
            font-weight:500;
            color:#FED7AA;
            margin:0 0 10px;
            line-height:1.5;
        }
        .subtitle {
            font-size:13px;
            color:rgba(255,255,255,0.65);
            margin:0 0 36px;
        }
        .pills {
            display:flex;
            gap:10px;
            justify-content:center;
            flex-wrap:wrap;
        }
        .pill {
            background:rgba(255,255,255,0.18);
            border:1px solid rgba(255,255,255,0.3);
            border-radius:20px;
            padding:7px 18px;
            font-size:12px;
            color:#fff;
            font-weight:500;
        }

        /* Stats Section */
        .stats {
            display:grid;
            grid-template-columns:repeat(4,1fr);
            gap:14px;
            padding:20px 24px 0;
            max-width:960px;
            margin:0 auto;
        }
        .stat-card {
            background:#FFF7ED;
            border:1px solid #FB923C;
            border-radius:14px;
            padding:20px 12px;
            text-align:center;
            transition:transform 0.2s ease;
        }
        .stat-card:hover { transform:translateY(-5px); }
        .stat-num {
            font-size:32px;
            font-weight:800;
            color:#7C2D00;
        }
        .stat-label {
            font-size:11px;
            color:#C2410C;
            margin-top:4px;
            font-weight:500;
        }

        /* How it works */
        .how {
            background:#FFF7ED;
            border:1px solid #FDBA74;
            border-radius:14px;
            padding:24px;
            margin:16px 24px 0;
            max-width:912px;
            margin-left:auto;
            margin-right:auto;
        }
        .how h3 {
            font-size:14px;
            font-weight:600;
            color:#7C2D00;
            margin:0 0 18px;
            text-align:center;
            letter-spacing:0.5px;
        }
        .flow-row {
            display:flex;
            align-items:center;
            justify-content:center;
            flex-wrap:wrap;
            gap:8px;
            font-size:12px;
        }
        .flow-box {
            border-radius:8px;
            padding:10px 16px;
            font-weight:600;
            min-width:80px;
            text-align:center;
        }
        .flow-arrow { color:#EA580C; font-size:20px; font-weight:700; }

        /* Bottom grid */
        .bottom-grid {
            display:grid;
            grid-template-columns:1fr 1fr;
            gap:14px;
            padding:16px 24px 0;
            max-width:960px;
            margin:0 auto;
        }
        .grid-card {
            background:#ffffff;
            border:1px solid #FDBA74;
            border-radius:14px;
            padding:20px;
        }
        .grid-title {
            font-size:13px;
            font-weight:600;
            color:#7C2D00;
            margin-bottom:14px;
        }
        .tech-pills { display:flex; flex-wrap:wrap; gap:7px; }
        .tech-pill {
            background:#FFF7ED;
            color:#C2410C;
            border:1px solid #FDBA74;
            font-size:11px;
            padding:5px 12px;
            border-radius:20px;
            transition:transform 0.2s;
        }
        .tech-pill:hover { transform:scale(1.05); }
        .highlight-item {
            display:flex;
            align-items:center;
            gap:8px;
            font-size:12px;
            color:#555;
            line-height:2;
        }
        .dot {
            width:7px; height:7px;
            border-radius:50%;
            background:#EA580C;
            display:inline-block;
            flex-shrink:0;
        }

        /* Status bar */
        .status-bar {
            background:linear-gradient(135deg,#7C2D00,#EA580C);
            border-radius:14px;
            padding:20px;
            margin:16px 24px 24px;
            max-width:912px;
            margin-left:auto;
            margin-right:auto;
            text-align:center;
        }
        .status-label { font-size:13px; color:#FED7AA; font-weight:500; }
        .status-row {
            display:flex;
            align-items:center;
            justify-content:center;
            gap:8px;
            margin-top:8px;
        }
        .green-dot {
            width:10px; height:10px;
            border-radius:50%;
            background:#4ADE80;
            animation: shimmer 1.5s ease-in-out infinite;
        }
        .status-text { color:#ffffff; font-size:15px; font-weight:600; }
        .status-footer {
            font-size:11px;
            color:rgba(255,255,255,0.55);
            margin-top:8px;
        }

        /* Animations */
        @keyframes float {
            0%,100%{ transform:translateY(0); }
            50%{ transform:translateY(-8px); }
        }
        @keyframes shimmer {
            0%,100%{ opacity:0.6; }
            50%{ opacity:1; }
        }

        /* Responsive */
        @media(max-width:600px){
            h1 { font-size:28px; }
            h2 { font-size:16px; }
            .stats { grid-template-columns:repeat(2,1fr); }
            .bottom-grid { grid-template-columns:1fr; }
        }
    </style>
</head>
<body>

    <!-- Hero -->
    <div class="hero">
        <div class="badge">D.Y. PATIL INTERNATIONAL UNIVERSITY</div>
        <span class="cloud-icon">☁</span>
        <h1>Welcome to DYPIU</h1>
        <div class="divider"></div>
        <h2>AI-Based Serverless Predictive<br>Auto-Scaler for Cloud Applications</h2>
        <p class="subtitle">Final Year Project — Computer Engineering 2025–26</p>
        <div class="pills">
            <span class="pill">Azure Functions</span>
            <span class="pill">Python AI</span>
            <span class="pill">Serverless Cloud</span>
            <span class="pill">Predictive Scaling</span>
        </div>
    </div>

    <!-- Stats -->
    <div class="stats">
        <div class="stat-card">
            <div class="stat-num">5 min</div>
            <div class="stat-label">Prediction interval</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">70%</div>
            <div class="stat-label">CPU scale threshold</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">AI</div>
            <div class="stat-label">Predictive engine</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">24/7</div>
            <div class="stat-label">Live monitoring</div>
        </div>
    </div>

    <!-- How it works -->
    <div class="how" style="margin-top:16px;">
        <h3>HOW IT WORKS</h3>
        <div class="flow-row">
            <div class="flow-box" style="background:#EA580C;color:#fff;">User traffic</div>
            <span class="flow-arrow">→</span>
            <div class="flow-box" style="background:#C2410C;color:#fff;">Web App</div>
            <span class="flow-arrow">→</span>
            <div class="flow-box" style="background:#9A3412;color:#fff;">Azure Monitor</div>
            <span class="flow-arrow">→</span>
            <div class="flow-box" style="background:#7C2D00;color:#FED7AA;">AI Predict</div>
            <span class="flow-arrow">→</span>
            <div class="flow-box" style="background:linear-gradient(135deg,#EA580C,#FB923C);color:#fff;">Auto Scale</div>
        </div>
    </div>

    <!-- Bottom Grid -->
    <div class="bottom-grid">
        <div class="grid-card">
            <div class="grid-title">Tech Stack</div>
            <div class="tech-pills">
                <span class="tech-pill">Azure Functions</span>
                <span class="tech-pill">Python 3.11</span>
                <span class="tech-pill">Flask</span>
                <span class="tech-pill">Azure Monitor</span>
                <span class="tech-pill">Blob Storage</span>
                <span class="tech-pill">App Service S1</span>
            </div>
        </div>
        <div class="grid-card">
            <div class="grid-title">Project Highlights</div>
            <div class="highlight-item"><span class="dot"></span>Scales BEFORE demand hits</div>
            <div class="highlight-item"><span class="dot"></span>Reduces latency by up to 40%</div>
            <div class="highlight-item"><span class="dot"></span>Zero idle cost — serverless</div>
            <div class="highlight-item"><span class="dot"></span>Time-series AI prediction model</div>
        </div>
    </div>

    <!-- Status Bar -->
    <div class="status-bar">
        <div class="status-label">App Status</div>
        <div class="status-row">
            <div class="green-dot"></div>
            <span class="status-text">Running and being monitored</span>
        </div>
        <div class="status-footer">
            D.Y. Patil International University — Computer Engineering Final Year Project 2025–26
        </div>
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
