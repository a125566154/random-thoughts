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
        print('Signature: ',signature)
        timestamp = request.args.get('timestamp')
        print('timestamp: ',timestamp)
        nonce = request.args.get('nonce')
        print('nonce: ',nonce)
        echostr = request.args.get('echostr')
        print('echostr: ',echostr)
        token = '1qaz2wsxE'

        list = [token, timestamp, nonce]
        list.sort()

        temp = ''.join(list)
        sha1 = hashlib.sha1(temp.encode('utf-8'))
        #map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print('hashcode: ',hashcode)

        if hashcode == signature:
            return echostr
        else:
            return "Failed"
    else:
        print('POST Handler')
        return "success"
        # data = request.form['body']
        # print(data)
        # recMsg = receive.parse_json(data)
        # if recMsg.MsgType == 'text':
        #     toUser = recMsg.FromUserName
        #     fromUser = recMsg.ToUserName
        #     content = "Response text"
        #     resMsg = reply.TextMsg(fromUser, toUser, content)
        #     return resMsg.send()
        # else:
        #     return "This is wx POST handler!"

def TextHandler(request):
    pass