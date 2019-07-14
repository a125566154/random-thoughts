from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import receive, reply

bp = Blueprint('resume', __name__, url_prefix='/resume')

@bp.route('/<username>', methods=['GET',])
def handle(username):
    return render_template('resume/index.html', name = username.capitalize())