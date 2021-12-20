from os import makedirs

from prometheus_flask_exporter import PrometheusMetrics


metrics = PrometheusMetrics.for_app_factory()


def create_metrics_dir():
    """Create directory to store cached Prometheus metrics."""
    from bisellium.settings import PROMETHEUS_MULTIPROC_DIR

    try:
        makedirs(PROMETHEUS_MULTIPROC_DIR)
    except FileExistsError:
        pass


def init_extensions(app):
    """Initialize extensions."""
    create_metrics_dir()
    metrics.init_app(app)
