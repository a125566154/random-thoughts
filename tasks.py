from flask_app.wechat import wx
from datetime import datetime

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

if __name__ == '__main__':
    from flask_app import create_app
    app = create_app()
    with app.app_context():
        drinkReminder()