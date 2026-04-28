from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>AI Autoscaler Demo App</h1>
    <p>This app is being monitored and autoscaled using Azure Functions + AI prediction.</p>
    <p>Status: Running</p>
    '''

@app.route('/health')
def health():
    return {"status": "healthy", "app": "autoscaler-demo"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
