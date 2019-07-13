# -*- coding: utf-8 -*-# filename: receive.py
import xml.etree.ElementTree as ET
import json

def parse_json(data):
    if len(data) == 0:
        return None
    jsonData = json.loads(data)
    msg_type = jsonData['MsgType']
    if msg_type == 'text':
        return TextMsg(jsonData)
    elif msg_type == 'image':
        return ImageMsg(jsonData)
        
class Msg(object):
    def __init__(self, jsonData):
        self.ToUserName = jsonData['ToUserName']
        self.FromUserName = jsonData['FromUserName']
        self.CreateTime = jsonData['CreateTime']
        self.MsgType = jsonData['MsgType']
        self.MsgId = jsonData['MsgId']
        
class TextMsg(Msg):
    def __init__(self, jsonData):
        Msg.__init__(self, jsonData)
        self.Content = jsonData['Content'].encode("utf-8")
        
class ImageMsg(Msg):
    def __init__(self, jsonData):
        Msg.__init__(self, jsonData)
        self.PicUrl = jsonData['PicUrl']
        self.MediaId = jsonData['MediaId']