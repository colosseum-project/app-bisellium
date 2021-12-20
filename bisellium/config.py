from os import environ


PROMETHEUS_MULTIPROC_DIR = environ.get(
    "PROMETHEUS_MULTIPROC_DIR", default="./prometheus_metrics"
)
LUDUS_URL = environ.get("LUDUS_URL", default="http://localhost:8080")
