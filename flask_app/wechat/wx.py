from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import receive, reply
from flask_app.models import db, Token

import hashlib
import requests
import json
import datetime

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
        data = request.data
        print(data)
        recMsg = receive.parse_xml(data)
        print('Message received successfully')
        res = getResponse(recMsg)
        return res

def getResponse(recMsg):
    if recMsg.MsgType == 'text':
        print('text message')
        toUser = recMsg.FromUserName
        fromUser = recMsg.ToUserName
        content = "Response text"
        resMsg = reply.TextMsg(toUser, fromUser, content)
        return resMsg.send()
    else:
        return "success"

@bp.route('/token',methods=['GET'])
def getAccessToken():
    token = Token.query.first()
    if token is None:
        t = getRealAccessToken()
        db.session.add(t)
        db.session.commit()
        return t.token
    else:
        now = datetime.datetime.now()
        print(now)
        print(token.expireon)
        print(now > token.expireon)
        if now > token.expireon :
            t = getRealAccessToken()
            db.session.add(t)
            db.session.delete(token)
            db.session.commit()
            print("t's token is %s" % (t.token))
            return t.token
        else:
            return token.token

def getRealAccessToken():
    appid = 'wxfc1a67f2d7bccbc7'
    secret = 'fc4bfaf80bf1cb4cc64183420fc6359e'
    response = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appid, secret))
    res = json.loads(response.content)
    res_token = res['access_token']
    res_expireon = datetime.datetime.now() + datetime.timedelta(seconds = int(res['expires_in']))
    token = Token(token = res_token, expireon = res_expireon)
    return token
        
def sendTemplateMessage(toUser, templateId, data):
    access_token = getAccessToken()
    print("token get %s" % (access_token))
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s' % (access_token)
    msgData = json.dumps({
        "touser" : toUser,
        "template_id" : templateId,
        "data" : data
    })
    res = requests.post(url, data = msgData)
    print(res.content)