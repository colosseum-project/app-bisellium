from flask import Flask

from bisellium.extensions import init_extensions


def create_app():
    """Create Flask application."""
    app = Flask(__name__)

    # apply configuration settings
    app.config.from_object("bisellium.settings")
    app.logger.info(f'Ludus API server URL set to "{app.config["LUDUS_URL"]}"')

    # initialize extensions
    init_extensions(app)

    # register views
    from bisellium.views import (
        healtcheck,
        errors,
        home,
        actadiurna,
        gladiatores,
        misc,
    )

    app.register_blueprint(errors.bp)
    app.register_blueprint(healtcheck.bp)
    app.register_blueprint(home.bp)
    app.register_blueprint(actadiurna.bp)
    app.register_blueprint(gladiatores.bp)
    app.register_blueprint(misc.bp)

    # return the freshly baked application!
    return app
