import os
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics.for_app_factory()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # ensure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ensure the Prometheus directory exists
    try:
        os.makedirs(os.environ.get("PROMETHEUS_MULTIPROC_DIR"))
    except OSError:
        pass

    # initialize Prometheus metrics
    metrics.init_app(app)

    with app.app_context():
        from bisellium import home
        from bisellium import gladiatores
        from bisellium import misc

        app.register_blueprint(home.bp)
        app.register_blueprint(gladiatores.bp)
        app.register_blueprint(misc.bp)

    return app
