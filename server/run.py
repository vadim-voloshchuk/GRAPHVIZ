from app import app
from common.pereferences import DEBUG, PORT, HOST, THREADED

from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)

app.run(HOST, PORT, debug=DEBUG, threaded=THREADED)