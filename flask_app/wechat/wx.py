from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import receive, reply

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
        data = request.form['body']
        recMsg = receive.parse_json(data)
        if recMsg.MsgType == 'text':
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            content = "Response text"
            resMsg = reply.TextMsg(fromUser, toUser, content)
            return resMsg.send()
        else:
            return "This is wx POST handler!"

def TextHandler(request):
    pass