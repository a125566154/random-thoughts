from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import receive, reply

import json

bp = Blueprint('resume', __name__, url_prefix='/resume')

@bp.route('/<username>', methods=['GET',])
def handle(username):
    with bp.open_resource('data.json') as json_file:
        data = json.load(json_file)
        cary_resume = data["resumeList"]["cary"]
    return render_template('resume/index.html', data = cary_resume)