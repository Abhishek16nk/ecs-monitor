# app.py
from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import prometheus_client
# Initialize Flask app
app = Flask(__name__)
# Initialize Prometheus metrics
REQUEST_COUNT = Counter(
'app_request_count',
'Application Request Count',
['method', 'endpoint', 'http_status']
)
RANDOM_COUNT = Counter(
'app_random_counter',
'Increment counter for demo'
)
# Disable default metrics
prometheus_client.REGISTRY.unregister(prometheus_client.PROCESS_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.PLATFORM_COLLECTOR)
prometheus_client.REGISTRY.unregister(prometheus_client.GC_COLLECTOR)
@app.route('/')
def hello():
REQUEST_COUNT.labels(
method='GET',
endpoint='/',
http_status=200
).inc()
return 'Hello World!'
@app.route('/increment')
def increment():
RANDOM_COUNT.inc()
REQUEST_COUNT.labels(
method='GET',
endpoint='/increment',
http_status=200
).inc()
return 'Counter incremented!'
@app.route('/metrics')
def metrics():
return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}
if __name__ == '__main__':
app.run(host='0.0.0.0', port=8080
