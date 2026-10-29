from flask import render_template
from blueprints.error import error_bp

@error_bp.app_errorhandler(404)
def error_404(error):
    return render_template('error/404.html'), 404

@error_bp.app_errorhandler(500)
def error_500(error):
    return render_template('error/500.html'), 500