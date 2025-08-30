from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Example metric
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Hello from Flask CI/CD App!"

# Metrics endpoint for Prometheus
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
