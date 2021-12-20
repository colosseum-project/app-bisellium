from os import makedirs

from prometheus_flask_exporter import PrometheusMetrics

from bisellium.config import PROMETHEUS_MULTIPROC_DIR

metrics = PrometheusMetrics.for_app_factory()


def init_metrics_dir():
    try:
        makedirs(PROMETHEUS_MULTIPROC_DIR)
    except FileExistsError:
        pass
