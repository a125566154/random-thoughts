import time

class Msg(object):
    def __init__(self):
        pass
    
    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)

class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, picUrl):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['PicUrl'] = picUrl
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        
        <PicUrl><![CDATA[{PicUrl}]]></PicUrl>
        
        </xml>
        """
        return XmlForm.format(**self.__dict)

class NewsMsg(Msg):
    def __init__(self, toUserName, fromUserName, title, desc, picUrl, link):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['title'] = title
        self.__dict['desc'] = desc
        self.__dict['picUrl'] = picUrl
        self.__dict['link'] = link

    def send(self):
        XmlForm = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[news]]></MsgType>
            <ArticleCount>1</ArticleCount>
            <Articles>
                <item>
                <Title><![CDATA[{title}]]></Title>
                <Description><![CDATA[{desc}]]></Description>
                <PicUrl><![CDATA[{picUrl}]]></PicUrl>
                <Url><![CDATA[{link}]]></Url>
                </item>
            </Articles>
        </xml>
        """
        print(XmlForm.format(**self.__dict))
        return XmlForm.format(**self.__dict)