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
        sleep(random.uniform(1, 3))
    return '<h1>Completed expensive database operation</h1>'
