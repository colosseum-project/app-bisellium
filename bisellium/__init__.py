from flask import Flask

from bisellium.extensions import metrics, init_metrics_dir
from bisellium.error_handlers import internal_server_error_handler
from bisellium.public import home, gladiatores, misc


def create_app():
    """Create Flask application."""
    app = Flask(__name__)

    app.config.from_pyfile("config.py")
    app.logger.info(f'Ludus URL set to "{app.config["LUDUS_URL"]}"')

    init_extensions(app)
    register_error_handlers(app)
    register_blueprints(app)

    return app


def init_extensions(app):
    """Register extensions."""
    init_metrics_dir()
    metrics.init_app(app)


def register_error_handlers(app):
    """Register error handlers."""
    app.register_error_handler(500, internal_server_error_handler)


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home.bp)
    app.register_blueprint(gladiatores.bp)
    app.register_blueprint(misc.bp)
