from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import receive, reply

import hashlib

bp = Blueprint('wx', __name__, url_prefix='/wx')

@bp.route('/',methods=['GET','POST'])
def handle():
    if request.method == 'GET':
        print('GET Handler')
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get('echostr')
        token = '1qaz2wsxE'

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr
        else:
            return "Failed"
    else:
        print('POST Handler')
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