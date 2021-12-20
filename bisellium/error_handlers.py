from flask import render_template


def internal_server_error_handler(e):
    return render_template("error/500.html", message=e), 500


def not_implemented_handler(e):
    return render_template("error/not-implemented.html"), 501
