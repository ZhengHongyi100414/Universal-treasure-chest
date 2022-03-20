import turtle
import datetime
import time    
def danwei():
    print('1·长度单位')
    print('2·数据单位')
    print('3·质量单位')
    print('4·体积（容积）单位')
    temp=int(input('请选择您需要的服务(1/2/3/4/5)。'))
    def cd():
        a=input('请输入原单位(mm/cm/dm/m/km：')
        b=int(input('请输入原数据：'))
        if a=='mm':
            print(b,'mm=',b/10,'cm=',b/100,'dm=',b/1000,'m=',b/1000000,'km')
        if a=='cm':
            print(b*10,'mm=',b,'cm=',b/10,'dm=',b/100,'m=',b/100000,'km')
        if a=='dm':
            print(b*100,'mm=',b*10,'cm=',b,'dm=',b/10,'m=',b/10000,'km')
        if a=='m':
            print(b*1000,'mm=',b*100,'cm=',b*10,'dm=',b,'m=',b/1000,'km')
        if a=='km':
            print(b*1000000,'mm=',b*100000,'cm=',b*10000,'dm=',b*1000,'m=',b,'km')
    def sg():
        a=input('请输入原单位(B/KB/MB/GB/TB：')
        b=int(input('请输入原数据：'))
        if a=='B':
            print(b,'B=',b/1204,'KB=',b/1204/1204,'MB=',b/1204/1204/1204,'GB=',b/1204/1204/1204/1204,'TB')
        if a=='KB':
            print(b*1024,'B=',b,'KB=',b/1204,'MB=',b/1204/1204,'GB=',b/1204/1204/1204,'TB')
        if a=='MB':
            print(b*1024*1024,'B=',b*1024,'KB=',b,'MB=',b/1204,'GB=',b/1204/1204,'TB')
        if a=='GB':
            print(b*1024*1024*1024,'B=',b*1024*1024,'KB=',b*1024,'MB=',b,'GB=',b/1204,'TB')
        if a=='TB':
            print(b*1024*1024*1024*1024,'B=',b*1024*1024*1024,'KB=',b*1024*1024,'MB=',b*1024,'GB=',b,'TB')
    def zl():
        a=input('请输入原单位(g/kg/t：')
        b=int(input('请输入原数据：'))
        if a=='g':
            print(b,'g=',b/1000,'kg=',b/1000/1000,'t')
        if a=='kg':
            print(b*1000,'g=',b,'kg=',b/1000,'t')
        if a=='t':
            print(b*1000*1000,'B=',b*1000,'kg=',b,'t')
    def tj():
        a=input('请输入原单位(ml/l：')
        b=int(input('请输入原数据：'))
        if a=='g':
            print(b,'ml=',b/1000,'l')
        if a=='kg':
            print(b*1000,'ml=',b,'l')
    if temp==1:
        cd()
    elif temp==2:
        sg()
    elif temp==3:
        zl()
    elif temp==4:
        tj()
    

def gongshi():
    print('功能开发中，即将开放。')
def geshui():
    print('个人所得税计算器')
    print('正在加载中，请稍等······')
    time.sleep(3)
    money=(int(input('请问您每月收入多少CNY？')))
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
    print("您每月需交",tax,"CNY","的个人所得税。")
def huobi():
    print('功能开发中，即将开放。')
def clock():
    print('如要退出，请重新启动程序！')
    time.sleep(2)
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

while True:
    print('欢迎来到超级百宝箱 1.4.8！')
    print('1·单位换算')
    print('2·常用公式计算')
    print('3·个人所得税计算')
    print('4·货币转换')
    print('5·时钟')
    print('6.天气')
    print(exit)
    temp=input('请选择您需要的服务(1/2/3/4/5/exit)。')
    if temp=='1':
        danwei()
    elif temp=='2':
        gongshi()
    elif temp=='3':
        geshui()
    elif temp=='4':
        huobi()
    elif temp=='5':
        clock()
    elif temp=='6':
        weather()
    elif temp=='exit':
        break