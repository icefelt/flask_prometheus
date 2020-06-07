from flask import Response, Flask
import prometheus_client
import time
import random
from prometheus_client import Counter
from prometheus_client import Histogram

app = Flask('prometheus-app')

@app.route('/metrics/')
def metrics():
    return Response(
        prometheus_client.generate_latest(),
        mimetype='text/plain; version=0.0.4; charset=utf-8'
    )

REQUESTS = Counter(
    'requests', 'Application Request Count',
    ['endpoint']
)

@app.route('/')
def index():
    REQUESTS.labels(endpoint='/').inc()
    return '<h1>Development Prometheus-backed Flash App</h1>'

TIMER = Histogram(
    'slow', 'Slow Requests',
    ['endpoint']
)

@app.route('/database/')
def database():
    with TIMER.labels('/database').time():
        time.sleep(random.uniform(1, 3))
    return '<h1>Completed expensive database operation</h1>'

from prometheus_client import start_http_server, Summary

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
