from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import receive

bp = Blueprint('wx', __name__, url_prefix='/wx')

@bp.route('/',methods=['GET','POST'])
def handle():
    if request.method == 'GET':
        print(request.args.get('key'))
        return "This is wx GET handler!"
    else:
        print(request.form)
        TextHandler(request)
        return "This is wx POST handler!"

def TextHandler(request):
    pass