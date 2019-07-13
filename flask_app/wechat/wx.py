from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import receive

bp = Blueprint('wx', __name__, url_prefix='/wx')

@bp.route('/',methods=['GET','POST'])
def handle():
    if request.method == 'GET':
        print(request.args.get('key'))
        try:
            parse_xml("")
        except:
            pass
        return "This is wx GET handler!"
    else:
        print(request.form)
        try:
            parse_xml("")
        except:
            pass
        TextHandler(request)
        return "This is wx POST handler!"

def TextHandler(request):
    pass