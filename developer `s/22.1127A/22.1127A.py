# coding= utf_8
import turtle
import datetime
import time
import requests
import pyqrcode
import socket
#import json 
import easygui as gui
import pyttsx3
from faker import Faker
import pyjokes


api_key='9677ca14-c723-4a20-9d58-e0a1d2413958'
def danwei():
    #gui.msgbox(msg='功能开发中，即将开放。', title='单位换算', ok_button='确认', image=None, root=None)
    temp=gui.choicebox(msg='请选择您需要的服务', title='单位换算', choices=['长度单位','数据单位','质量单位','体积（容积）单位'])
    def cd():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['mm','cm','dm','m','km'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='mm':
            gui.msgbox(msg=str(b)+'mm='+str(b/10)+'cm='+str(b/100)+'dm='+str(b/1000)+'m='+str(b/1000000)+'km', title='单位换算', ok_button='确认', image=None, root=None),
        if a=='cm':
            gui.msgbox(msg=str(b*10)+'mm='+str(b)+'cm='+str(b/10)+'dm='+str(b/100)+'m='+str(b/100000)+'km', title='单位换算', ok_button='确认', image=None, root=None)
        if a=='dm':
            gui.msgbox(msg=str(b*100)+'mm='+str(b*10)+'cm='+str(b)+'dm='+str(b/10)+'m='+str(b/10000)+'km', title='单位换算', ok_button='确认', image=None, root=None)
        if a=='m':
            gui.msgbox(msg=str(b*1000)+'mm='+str(b*100)+'cm='+str(b*10)+'dm='+str(b)+'m='+str(b/1000)+'km', title='单位换算', ok_button='确认', image=None, root=None)
        if a=='km':
            gui.msgbox(msg=str(b*1000000)+'mm='+str(b*100000)+'cm='+str(b*10000)+'dm='+str(b*1000)+'m='+str(b)+'km', title='单位换算', ok_button='确认', image=None, root=None)
    def sg():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['B','KB','MB','GB','TB'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='B':
            gui.msgbox(msg=str(b)+'B='+str(b/1024)+'KB='+str(b/1024/1024)+'MB='+str(b/1024/1024/1024)+'GB='+str(b/1024/1024/1024/1024)+'TB', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='KB':
            gui.msgbox(msg=str(b*1024)+'B='+str(b)+'KB='+str(b/1024)+'MB='+str(b/1024/1024)+'GB='+str(b/1024/1024/1024)+'TB', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='MB':
            gui.msgbox(msg=str(b*1024*1024)+'B='+str(b*1024)+'KB='+str(b)+'MB='+str(b/1024)+'GB='+str(b/1024/1024)+'TB', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='GB':
            gui.msgbox(msg=str(b*1024*1024*1024)+'B='+str(b*1024*1024)+'KB='+str(b*1024)+'MB='+str(b)+'GB='+str(b/1024)+'TB', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='TB':
            gui.msgbox(msg=str(b*1024*1024*1024*1024)+'B='+str(b*1024*1024*1024)+'KB='+str(b*1024*1024)+'MB='+str(b*1024)+'GB='+str(b)+'TB', title='单位换算', ok_button=' ', image=None, root=None)
    def zl():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['g','kg','t'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='g':
            gui.msgbox(msg=str(b)+'g='+str(b/1000)+'kg='+str(b/1000/1000)+'t', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='kg':
            gui.msgbox(msg=str(b*1000)+'g='+str(b)+'kg='+str(b/1000)+'t', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='t':
            gui.msgbox(msg=str(b*1000*1000)+'B='+str(b*1000)+'kg='+str(b)+'t', title='单位换算', ok_button=' ', image=None, root=None)
    def tj():
        a=gui.choicebox(msg='请选择原单位', title='单位换算', choices=['ml','l'])
        b=int(gui.enterbox(msg='请输入原数据？', title='单位换算', default='', strip=True, image=None, root=None))
        if a=='g':
            gui.msgbox(msg=str(b)+'ml='+str(b/1000)+'l', title='单位换算', ok_button=' ', image=None, root=None)
        if a=='kg':
            gui.msgbox(msg=str(b*1000)+'ml='+str(b)+'l', title='单位换算', ok_button=' ', image=None, root=None)
    if temp=='长度单位':
        cd()
    elif temp=='数据单位':
        sg()
    elif temp=='质量单位':
        zl()
    elif temp=='体积（容积）单位':
        tj()
def gongshi():
    print('功能开发中，即将开放。')
def geshui():
    #print('个人所得税计算器')
    #print('正在加载中，请稍等······')
    #money=(int(input('请问您每月收入多少CNY？')))
    money=int(gui.enterbox(msg='请问您每月收入多少CNY？', title='个人所得税计算器', default='', strip=True, image=None, root=None))
    if money<=5000:
        tax=0
    elif money-5000<=1500:
        tax=(money-5000)*0.03-0
    elif money-5000>1500 and money-5000<=4500:
        tax=(money-5000)*0.1-105
    elif money-5000>4500 and money-5000<=9000:
        tax=(money-5000)*0.2-555
    elif money-5000>9000 and money-5000<=35000:
        tax=(money-5000)*0.25-1005
    elif money-5000>35000 and money-5000<=55000:
        tax=(money-5000)*0.3-2755
    elif money-5000>55000 and money-5000<=80000:
        tax=(money-5000)*0.35-5505
    elif money-5000>80000:
        tax=(money-5000)*0.45-13505
    #print("您每月需交",str(tax),"CNY","的个人所得税。")
    gui.msgbox(msg="您每月需交"+str(tax)+"CNY"+"的个人所得税。", title='个人所得税计算器', ok_button='退出', image=None, root=None)
def huobi():
    currency_code=['CNY 人民币','HKD 港币','USD 美元','EUR 欧元','GBP 英镑','JPY 日元','DEM 德国马克','SGD 新加坡元']
    original=gui.choicebox(msg='请选择您需要换算的原单位', title='货币换算', choices=currency_code)
    target=gui.choicebox(msg='请选择您需要换算的目标单位', title='货币换算', choices=currency_code)
    num=int(gui.enterbox(msg='请输入原数据', title='货币换算', default='', strip=True, image=None, root=None))
    url = "https://v6.exchangerate-api.com/v6/83c890b38cbb97afed2a8db0/latest/"+original[0]+original[1]+original[2]
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    print(a)
    b=a["conversion_rates"]
    c=b[target[0]+target[1]+target[2]]
    gui.msgbox(msg=str(num)+original[0]+original[1]+original[2]+'='+str(num*c)+target[0]+target[1]+target[2], title='货币换算', ok_button='确定', image=None, root=None)
def clock():
    gui.msgbox(msg='如要退出，请重新启动程序！', title='时钟', ok_button='确定', image=None, root=None)
    t=turtle.Turtle()
    t.speed(0)
    def board(r):#绘制表盘
        t.penup()
        t.setheading(270)
        t.fd(r)
        t.setheading(0)
        t.pendown()
        t.circle(r)
        t.penup()
        t.home()
        t.pendown()
        t.dot()
    def num(r):#写数字，打点
        board(r)
        t.setheading(60)
        for i in range(12):
            t.penup()
            t.fd(r)
            t.pendown()
            t.write(i+1)
            t.dot()
            t.penup()
            t.backward(r)
            t.right(30)
            t.hideturtle()
    def hms(r):#画针
        h=turtle.Turtle()
        m=turtle.Turtle()
        s=turtle.Turtle()
        h.speed(-2)
        m.speed(-2)
        s.speed(-2)
        timing=0
        while True:            
            ti=datetime.datetime.now()
            angles=[]
            h.pendown()
            m.pendown()
            s.pendown()
            hmsGUI=[h,m,s]
            h_angle = -ti.hour*30-ti.minute*(30/60)-ti.second*(30/60/60)+90
            m_angle=-ti.minute*6-ti.second*(6/60)+90
            s_angle=-ti.second*6+90
            angles=[h_angle,m_angle,s_angle]
            for i in range(3):
                hmsGUI[i].pensize(7-2*(i+1))
                hmsGUI[i].setheading(angles[i])
                hmsGUI[i].fd(((i+1)*0.3)*r)
            turtle.tracer(1) 
            time.sleep(1)
            turtle.tracer(0)

            h.clear()
            m.clear()
            s.clear()
            h.penup()
            m.penup()
            s.penup()
            h.home()
            m.home()
            s.home()
            timing=timing+1
            if timing>=3600:
                turtle.bye()
    num(200)     
    hms(200)
def weather():
    global api_key
    gui.msgbox(msg='因为API接口位于外国，您可能需要等待5~10秒。谢谢谅解！',title='ip地址', ok_button='确定', image=None, root=None)
    url='http://api.airvisual.com/v2/countries?key='+api_key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=[]
    for i in range(len(b)):
        c.append(b[i]['country'])
    cou=gui.choicebox(msg='请选择您需要查询的国家', title='天气', choices=c)
    
    url='http://api.airvisual.com/v2/states?country='+cou+'&key='+api_key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=[]
    for i in range(len(b)):
        c.append(b[i]['state'])
    sta=gui.choicebox(msg='请选择您需要查询的省份（州）', title='天气', choices=c)
    
    url='http://api.airvisual.com/v2/cities?state='+sta+'&country='+cou+'&key='+api_key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=[]
    for i in range(len(b)):
        c.append(b[i]['city'])
    cit=gui.choicebox(msg='请选择您需要查询的城市', title='天气', choices=c)
    url = "http://api.airvisual.com/v2/city?city="+cit+"&state="+sta+"&country="+cou+"&key="+api_key
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    a=response.json()
    b=a['data']
    c=b['current']
    d=c['weather']
    e='当前时间戳：'+str(d['ts'])+'  '+cou+','+sta+','+cit+'  '+'当前气温为：'+str(d['tp'])+'摄氏度 气压为：'+str(d['pr'])+'百帕 风速为'+str(d['ws'])+'m/s 风向为：'+str(d['wd'])+'度'
    gui.msgbox(msg=e, title='天气', ok_button='确定', image=None, root=None)
def ip():
    gui.msgbox(msg='因为API接口位于外国，您可能需要等待5~10秒。谢谢谅解！',title='ip地址', ok_button='点击以开始', image=None, root=None)
    def get_host_ip():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    response=requests.get('http://ip-api.com/json/?lang=zh-CN')
    dictr=response.json()
    weidu=''
    jingdu=''
    if dictr['lat']>0:
        weidu='北纬'+str(dictr['lat'])+'度'
    elif dictr['lat']==0:
        weidu="0度"
    else:
        weidu='北纬'+str(dictr['lat']*(-1))+'度'
    if dictr['lon']>0:
        jingdu='东经'+str(dictr['lon'])+'度'
    elif dictr['lon']==0:
        jingdu="0度"
    else:
        jingdu='西经'+str(dictr['lon']*(-1))+'度'
    gui.msgbox(msg='当前内网ip为：'+get_host_ip()+'  , 当前所在局域网的公网ip地址为'+dictr['query']+'  , 地址为：'+dictr['country']+' '+dictr['regionName']+' '+dictr['city']+'  , 经纬度为'+jingdu+' '+weidu+'  , 时区为：'+dictr['timezone']+'  , ISP运营商为：'+dictr['isp'],title='ip地址', ok_button='确定', image=None, root=None)
def read():
    gui.msgbox(msg="这是一个让您的txt文件变成朗读后的mp3文件的功能（它只支持英语！！！）现在，打开您的txt文件，然后再选择您的保存目录！",title='文件朗读', ok_button='确认', image=None, root=None)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    fo = open(gui.fileopenbox(msg='选择您的txt文件！', title='文件朗读', default='*.txt', filetypes=None, multiple=False), mode="r",encoding="utf-8")
    save=gui.filesavebox(msg='保存您的mp3文件！', title='文件朗读',default='audio.mp3', filetypes=None)
    engine.save_to_file(fo.read(),save )
    gui.msgbox(msg='现在去'+save+'聆听您的文档吧！',title='文档朗读',ok_button='我知道了！', image=None, root=None)	
def fake_profile():
    gui.msgbox(msg='在这个功能中，我们将为您生成一个虚拟的身份信息，您可以在各个社交平台上使用它。点击开始生成！',title='虚拟身份', ok_button='开始！', image=None, root=None)
    fake=Faker()
    pf=fake.profile()
    name=pf['name']
    company=pf['company']
    address=pf['residence']
    birthday=pf['birthdate']
    bg=str()
    if pf['blood_group']=='B-':
        bg='B'
    elif pf['blood_group']=='AB-':
        bg='AB'
    elif pf['blood_group']=='A-':
        bg='A'
    elif pf['blood_group']=='O-':
        bg='O'
    email=pf['mail']
    username=pf['username']
    if pf['sex']=='F':
        sex='女'
    elif pf['sex']=='M':
        sex='男'
    gui.msgbox(msg='在这虚拟身份体系中，您的名字为'+name+'，您的用户名为'+username+'，您的e-mail为'+email+'，您的生日是'+str(birthday)+'，您的住址为'+address+'，您的血型为'+bg+'型，您的性别为'+sex+'，您在'+company+'工作。',title='虚拟身份', ok_button='确定', image=None, root=None)
def qrcode():
    gui.msgbox(msg='这个功能可以帮您把文本（英语）转为可以扫描的二维码。',title='二维码生成',ok_button='让我们开始吧！')
    inpStr = gui.enterbox(msg='请输入二维码的内容（只支持英语！）', title='二维码生成', default='', strip=True, image=None, root=None)
    print(inpStr)
    qrc = pyqrcode.create(inpStr)
    qrc.png(gui.filesavebox(msg='请选择二维码保存路径！', title='二维码生成', default='QRCode.png', filetypes=None), scale=10)
def joke():
    gui.msgbox(msg='这个功能可以送给您一个有关程序员的笑话。但它是英语的！',title='笑一笑！',ok_button='让我康康！')
    gui.msgbox(msg=pyjokes.get_joke() ,title='笑一笑',ok_button='真好笑！')
def change_api_key():
    global api_key
    password=gui.passwordbox(msg='请输入密码', title='更改API Key', default=None, image=None, root=None)
    if password=='password':
        api_key=gui.enterbox(msg='请输入AirVisual(IQAir)的合法API Key。', title='更改API Key', default=api_key, strip=True, image=None, root=None)
def encrypt_information():
    
    gui.msgbox(msg='这个功能可以帮你加密一句话。但它仍然只支持英语！',title='信息加密',ok_button='让我们开始吧！',image=None,root=None)
while True:
    '''
    print('欢迎来到超级百宝箱 1.4.8！')
    print('1·单位换算')
    print('2·个人所得税计算')
    print('3·货币转换')
    print('4·时钟')
    print('5.天气')
    print(exit)
    temp=input('请选择您需要的服务(1/2/3/4/5/exit)。')
    if temp=='1':
        danwei()
    elif temp=='2':
        geshui()
    elif temp=='3':
        huobi()
    elif temp=='4':
        clock()
    elif temp=='5':
        weather()
    elif temp=='exit':
        break
    '''
    temp=gui.choicebox(msg='请选择您需要的服务', title='超级百宝箱 22.1127A', choices=['单位换算','个人所得税计算','货币转换','时钟','天气','IP地址查询','文件朗读','虚拟身份生成','二维码生成','笑一笑','更改API Key','exit'])
    print(temp)
    if temp=='单位换算':
        danwei()
    if temp=='个人所得税计算':
        geshui()
    elif temp=='货币转换':
        huobi()
    elif temp=='时钟':
        clock()
    elif temp=='天气':
        weather()
    elif temp=='IP地址查询':
        ip()
    elif temp=='文件朗读':
        read()
    elif temp=='虚拟身份生成':
        fake_profile()
    elif temp=='二维码生成':
        qrcode()
    elif temp=='笑一笑':
        joke()
    elif temp=='更改API Key':
        change_api_key()
    elif temp=='exit' or temp==None:
        break