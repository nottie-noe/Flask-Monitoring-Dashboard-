from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def dashboard():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return '''
    <html>
        <head>
            <title>CEEYIT Dashboard</title>
            <style>
                body { font-family: Arial; background: #fefefe; text-align: center; margin-top: 100px; }
                h1 { color: #2a9d8f; }
                p { font-size: 18px; color: #264653; }
            </style>
        </head>
        <body>
            <h1>CEEYIT Monitoring Dashboard</h1>
            <p>Your DevOps metrics will be visualized here.</p>
        </body>
    </html>
    '''

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
