from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_app.wechat import wx
from datetime import datetime

bp = Blueprint('task', __name__, url_prefix='/task')

@bp.route('/drinkReminder',methods=['GET'])
def drinkReminder():
    toUser = 'ocYwz5oq8kZxYTVFoCocZ4Sq_zog'
    templateId = 'lvB_ErsV-LFeRaJC56qfJbGcufxfWr5ArTlzdjfk0xA'
    data = {
        "fisrt" : {
            "value" : "Remember to Drink Your Water~",
            "color" : "#173177"
        },
        "now" : {
            "value" : datetime.now().strftime("%H:%M:%S"),
            "color" : "#173177"
        },
        "remark" : {
            "value" : "Drink Drink Better For Your Health!",
            "color" : "#173177"
        }
    }
    wx.sendTemplateMessage(toUser = toUser, templateId = templateId, data = data)
    return "success"