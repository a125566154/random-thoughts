from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import wx
from datetime import datetime

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/drinkReminder',methods=['GET'])
def drinkReminder():
    toUser = 'ocYwz5jS4kU8GuUZDM9KmYLsi99w'
    templateId = '6iyPcqFBw7-gm6QSqj9zjyZeRl-zM2FheCnB4xWkK34'
    data = {
        "first" : {
            "value" : "Remember to Drink Your Water~",
            "color" : "#173177"
        },
        "task" : {
            "value" : "8 cups of water a day makes all the pains away",
            "color" : "#173177"
        },
        "remark" : {
            "value" : "Drink Drink Better For Your Health!",
            "color" : "#173177"
        }
    }
    wx.sendTemplateMessage(toUser = toUser, templateId = templateId, data = data)
    return "success"