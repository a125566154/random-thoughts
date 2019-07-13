from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('wx', __name__, url_prefix='/wx')

@bp.route('/',methods=['GET','POST'])
def wx():
    if request.method == 'GET':
        print(request.args.get('key'))
        return "This is wx GET handler!"
    else:
        return "This is wx POST handler!"