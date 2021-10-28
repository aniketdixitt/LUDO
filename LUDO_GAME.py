import tkinter
from tkinter import *
import random

class home:
    def __init__(self,r):
        self.c=Canvas(r,width=800,height=660,bg="black")
        self.c.pack()
        self.p=PhotoImage(file="logo.png")
        self.c.create_image(300,10,image=self.p,anchor=NW)
        self.p2=PhotoImage(file="d2.png")
        self.c.create_image(80,220,image=self.p2,anchor=NW)
        self.p3=PhotoImage(file="d2.png")
        self.c.create_image(520,220,image=self.p3,anchor=NW)
        a=random.randint(0,9)
        b=random.randint(65,90)
        c=random.randint(11,99)
        d=random.randint(97,122)
        aa=str(a)
        bb=str(chr(b))
        cc=str(c)
        dd=str(chr(d))
        self.no=aa+bb+cc+dd
        self.l1=Label(self.c,text=self.no,bg="indian red",font=("Cooper black",30))
        self.l1.place(x=330,y=400)
        self.e1=Entry(self.c,width=20,bg="steelblue3",font=("Cooper black",14))
        self.e1.place(x=280,y=500)
        self.b=Button(self.c,text="ENTER\nCAPTCHA",font=("Cooper black",14),bg="wheat3",command=lambda: self.getdetails())
        self.b.place(x=330,y=550)
        self.b.bind("<Return>", lambda:self.getdetails())

        
    def getdetails(self):
        self.g1=self.e1.get()
        if self.g1==self.no:
            r.destroy()
            r1=Tk()
            e=enter(r1)
            r1.title("LUDO KNIGHT")
            r1.mainloop()
        else:
            rn=Tk()
            self.w=Canvas(rn,height=300,width=300,bg="black")
            self.w.pack()
            self.w1=Label(self.w,text="Wrong captcha entered!",bg="indian red",font=("Cooper black",14))
            self.w1.pack()
            rn.mainloop()

class enter:
    def __init__(self,r1):
        self.c1=Canvas(r1,width=800,height=660,bg="black")
        self.c1.pack()
        self.p=PhotoImage(file="logo.png")
        self.c1.create_image(300,10,image=self.p,anchor=NW)
        self.p2=PhotoImage(file="d2.png")
        self.c1.create_image(80,220,image=self.p2,anchor=NW)
        self.p3=PhotoImage(file="d2.png")
        self.c1.create_image(520,220,image=self.p3,anchor=NW)

        self.b1=Button(self.c1,text="PLAY\nGAME",font=("Cooper black",14),bg="wheat3",height=3,width=6,command=lambda: self.play())
        self.b1.place(x=350,y=510)
        self.b2=Button(self.c1,text="CREDITS",font=("Cooper black",14),bg="indian red",command= lambda: self.cr())
        self.b2.place(x=550,y=510)
        self.b2=Button(self.c1,text="HOW TO\nPLAY",font=("Cooper black",14),bg="steelblue3",command= lambda: self.hp())
        self.b2.place(x=120,y=510)
        self.w2=Label(self.c1,text="WELCOME!",bg="lightgreen",font=("Cooper black",20))
        self.w2.place(x=300,y=400)
    def play(self):
        r2=Tk()
        l=Ludo(r2)
        r2.title("LUDI KNIGHT")
        r2.mainloop()
    def cr(self):
        a="\tTHIS PROJECT HAS BEEN CREATED BY:\n\n\n"
        b="\t ANIKET DIXIT\n\n\n"
        c="\t UDAY PRATAP SINGH\n\n\n"
        d="\t ANKIT VATS\n\n\n"
        e="\t AMAN KUMAR\n\n\n"
        q=a+b+c+d+e
        ab=Tk()
        e=Canvas(ab,height=600,width=800,bg="salmon2")
        e.propagate(0)
        e.pack()
        e1=Label(e,text=q,fg="darkblue",bg="salmon2",font=("Cooper black",18))
        e1.place(x=10,y=0)
        ab.title("CREDITS OF THE GAME")
    def hp(self):
        a="\tRULES TO PLAY:\n\n\n"
        b="1)Tokken will only open after you score a 6."
        b1="\n2)There will be no extra turn given for scoring 6,\n therefore game will beplayed smoothly."
        c1="\n3)After evey click on dice make sure to click on your tokken \nto make sure the colored area gets back to its normal color."
        c2="\n4)This game can only be played by 2 players. Neither more than\n 2 nor less than 2."
        c="\n5)At the end of the game, the winners will be announced as soon\n as all the 4 tokkens get inside home for a player."
        d="\n6)Yellow will be player 1 and red will be player 2."
        q=a+b+b1+c1+c2+c+d
        ab=Tk()
        e=Canvas(ab,height=500,width=600,bg="salmon2")
        e.propagate(0)
        e.pack()
        e1=Label(e,text=q,fg="darkblue",bg="salmon2",font=15)
        e1.place(x=10,y=0)
        ab.title("RULES OF THE GAME")

        
class Ludo:
    yval=0
    yto=0
    nomovey=0
    ttr=0
    
    def __init__(self,r2):
        self.f=Frame(r2,height=650,width=650,bg="pink")
        self.f.propagate(0)
        self.f.pack()
        self.c=Canvas(self.f,bg="blue",height=250,width=250,cursor="pencil")
        self.c1=Canvas(self.f,bg="red",height=250,width=250,cursor="pencil")
        self.c2=Canvas(self.f,bg="green",height=250,width=250,cursor="pencil")
        self.c3=Canvas(self.f,bg="yellow",height=250,width=250,cursor="pencil")

        self.b=self.c.create_rectangle(40,40,210,210,width=0,fill="white",activefill="paleturquoise2")    #white box inside blue
        self.r=self.c1.create_rectangle(40,40,210,210,width=0,fill="white",activefill="salmon1")          #white box inside red
        self.g=self.c2.create_rectangle(40,40,210,210,width=0,fill="white",activefill="olivedrab1")     #white box inside green
        self.y=self.c3.create_rectangle(40,40,210,210,width=0,fill="white",activefill="light goldenrod yellow")     #white box inside yellow

        self.cb1=self.c.create_oval(50,50,120,120,width=0,fill="blue")     #circle inside blue
        self.cb2=self.c.create_oval(130,50,200,120,width=0,fill="blue")
        self.cb3=self.c.create_oval(50,130,120,200,width=0,fill="blue")
        self.cb4=self.c.create_oval(130,130,200,200,width=0,fill="blue")

        self.cr1=self.c1.create_oval(50,50,120,120,width=0,fill="red")     #circle inside red
        self.rt1=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(5))     #button 1
        self.rt1.place(x=72,y=72)
        self.cr2=self.c1.create_oval(130,50,200,120,width=0,fill="red")
        self.rt2=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(6))     #button 2
        self.rt2.place(x=152,y=72)
        self.cr3=self.c1.create_oval(50,130,120,200,width=0,fill="red")
        self.rt3=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(7))        #button 3
        self.rt3.place(x=72,y=152)
        self.cr4=self.c1.create_oval(130,130,200,200,width=0,fill="red")
        self.rt4=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(8))           #button 4
        self.rt4.place(x=152,y=152)

        self.cg1=self.c2.create_oval(50,50,120,120,width=0,fill="green")     #circle inside green
        self.cg2=self.c2.create_oval(130,50,200,120,width=0,fill="green")
        self.cg3=self.c2.create_oval(50,130,120,200,width=0,fill="green")
        self.cg4=self.c2.create_oval(130,130,200,200,width=0,fill="green")

        self.cy1=self.c3.create_oval(50,50,120,120,width=0,fill="yellow")     #circle inside yellow
        self.yt1=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(1))     #button 1
        self.yt1.place(x=72,y=72)
        self.cy2=self.c3.create_oval(130,50,200,120,width=0,fill="yellow")
        self.yt2=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(2))     #button 2
        self.yt2.place(x=152,y=72)
        self.cy3=self.c3.create_oval(50,130,120,200,width=0,fill="yellow")
        self.yt3=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(3))        #button 3
        self.yt3.place(x=72,y=152)
        self.cy4=self.c3.create_oval(130,130,200,200,width=0,fill="yellow")
        self.yt4=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(4))           #button 4
        self.yt4.place(x=152,y=152)
       
        self.c.place(x=0,y=0)
        self.c1.place(x=396,y=0)
        self.c2.place(x=396,y=396)
        self.c3.place(x=0,y=396)

        self.box13=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box14=Canvas(self.f,bg="blue",height=40,width=47,cursor="pencil")
        self.box15=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box16=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box17=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box18=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box13.place(x=0,y=252)
        self.box14.place(x=40,y=252)
        self.box15.place(x=88,y=252)
        self.box16.place(x=128,y=252)
        self.box17.place(x=168,y=252)
        self.box18.place(x=208,y=252)
        self.box11=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box10=Canvas(self.f,bg="lightgrey",height=40,width=44,cursor="pencil")
        self.box9=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box9.create_text(20,20,fill="yellow",font="50,bold",text="Ѫ")
        self.box8=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box7=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box6=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box11.place(x=0,y=352)
        self.box10.place(x=42,y=352)
        self.box9.place(x=88,y=352)
        self.box8.place(x=128,y=352)
        self.box7.place(x=168,y=352)
        self.box6.place(x=208,y=352)
        self.box12=Canvas(self.f,bg="lightgrey",height=55,width=39,cursor="pencil")
        self.ai2=Canvas(self.f,bg="blue",height=55,width=45,cursor="pencil")
        self.ai3=Canvas(self.f,bg="blue",height=55,width=39,cursor="pencil")
        self.ai4=Canvas(self.f,bg="blue",height=55,width=39,cursor="pencil")
        self.ai5=Canvas(self.f,bg="blue",height=55,width=39,cursor="pencil")
        self.ai6=Canvas(self.f,bg="blue",height=55,width=40,cursor="pencil")
        self.box12.place(x=0,y=294)
        self.ai2.place(x=41,y=294)
        self.ai3.place(x=88,y=294)
        self.ai4.place(x=128,y=294)
        self.ai5.place(x=168,y=294)
        self.ai6.place(x=208,y=294)


        self.box26=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box27=Canvas(self.f,bg="red",height=40,width=40,cursor="pencil")
        self.box28=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box29=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box30=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box31=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box26.place(x=354,y=0)
        self.box27.place(x=354,y=42)
        self.box28.place(x=354,y=85)
        self.box29.place(x=354,y=127)
        self.box30.place(x=354,y=169)
        self.box31.place(x=354,y=211)
        self.box24=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box23=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box22=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box22.create_text(20,20,fill="darkblue",font="50,bold",text="Ѫ")
        self.box21=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box20=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box19=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box24.place(x=252,y=0)
        self.box23.place(x=252,y=42)
        self.box22.place(x=252,y=85)
        self.box21.place(x=252,y=127)
        self.box20.place(x=252,y=169)
        self.box19.place(x=252,y=211)
        self.box25=Canvas(self.f,bg="lightgrey",height=40,width=58,cursor="pencil")
        self.bi2=Canvas(self.f,bg="red",height=40,width=58,cursor="pencil")
        self.bi3=Canvas(self.f,bg="red",height=40,width=58,cursor="pencil")
        self.bi4=Canvas(self.f,bg="red",height=40,width=58,cursor="pencil")
        self.bi5=Canvas(self.f,bg="red",height=40,width=58,cursor="pencil")
        self.bi6=Canvas(self.f,bg="red",height=40,width=58,cursor="pencil")
        self.box25.place(x=294,y=0)
        self.bi2.place(x=294,y=42)
        self.bi3.place(x=294,y=85)
        self.bi4.place(x=294,y=127)
        self.bi5.place(x=294,y=169)
        self.bi6.place(x=294,y=211)


        self.box45=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box46=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box47=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box48=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box48.create_text(20,20,fill="darkgreen",font="50,bold",text="Ѫ")
        self.box49=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box50=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box45.place(x=354,y=396)
        self.box46.place(x=354,y=439)
        self.box47.place(x=354,y=482)
        self.box48.place(x=354,y=524)
        self.box49.place(x=354,y=566)
        self.box50.place(x=354,y=608)
        self.box5=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box4=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box3=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box2=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box1=Canvas(self.f,bg="yellow",height=40,width=40,cursor="pencil")
        self.box52=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box5.place(x=252,y=396)
        self.box4.place(x=252,y=439)
        self.box3.place(x=252,y=482)
        self.box2.place(x=252,y=524)
        self.box1.place(x=252,y=566)
        self.box52.place(x=252,y=608)
        self.bi1=Canvas(self.f,bg="yellow",height=40,width=58,cursor="pencil")
        self.bi2=Canvas(self.f,bg="yellow",height=40,width=58,cursor="pencil")
        self.bi3=Canvas(self.f,bg="yellow",height=40,width=58,cursor="pencil")
        self.bi4=Canvas(self.f,bg="yellow",height=40,width=58,cursor="pencil")
        self.bi5=Canvas(self.f,bg="yellow",height=40,width=58,cursor="pencil")
        self.box51=Canvas(self.f,bg="lightgrey",height=40,width=58,cursor="pencil")
        self.bi1.place(x=294,y=396)
        self.bi2.place(x=294,y=439)
        self.bi3.place(x=294,y=482)
        self.bi4.place(x=294,y=524)
        self.bi5.place(x=294,y=566)
        self.box51.place(x=294,y=608)


        self.box32=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box33=Canvas(self.f,bg="lightgrey",height=40,width=47,cursor="pencil")
        self.box34=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box35=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box35.create_text(20,20,fill="red",font="50,bold",text="Ѫ")
        self.box36=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box37=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box32.place(x=397,y=252)
        self.box33.place(x=439,y=252)
        self.box34.place(x=481,y=252)
        self.box35.place(x=523,y=252)
        self.box36.place(x=565,y=252)
        self.box37.place(x=607,y=252)
        self.box44=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box43=Canvas(self.f,bg="lightgrey",height=40,width=44,cursor="pencil")
        self.box42=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box41=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box40=Canvas(self.f,bg="green",height=40,width=40,cursor="pencil")
        self.box39=Canvas(self.f,bg="lightgrey",height=40,width=40,cursor="pencil")
        self.box44.place(x=397,y=352)
        self.box43.place(x=439,y=352)
        self.box42.place(x=481,y=352)
        self.box41.place(x=523,y=352)
        self.box40.place(x=565,y=352)
        self.box39.place(x=607,y=352)
        self.ai1=Canvas(self.f,bg="green",height=55,width=39,cursor="pencil")
        self.ai2=Canvas(self.f,bg="green",height=55,width=42,cursor="pencil")
        self.ai3=Canvas(self.f,bg="green",height=55,width=40,cursor="pencil")
        self.ai4=Canvas(self.f,bg="green",height=55,width=40,cursor="pencil")
        self.ai5=Canvas(self.f,bg="green",height=55,width=40,cursor="pencil")
        self.box38=Canvas(self.f,bg="lightgrey",height=55,width=40,cursor="circle")
        self.ai1.place(x=397,y=294)
        self.ai2.place(x=439,y=294)
        self.ai3.place(x=481,y=294)
        self.ai4.place(x=523,y=294)
        self.ai5.place(x=565,y=294)
        self.box38.place(x=607,y=294)



        self.bloc=Canvas(self.f,bg="orange",height=142,width=142)
        self.bl=self.bloc.create_polygon(0,0,70,70,0,145,fill="blue")
        self.ye=self.bloc.create_polygon(0,145,150,150,70,69,fill="yellow")
        self.gr=self.bloc.create_polygon(145,0,150,150,70,70,fill="green")
        self.rd=self.bloc.create_polygon(0,0,145,0,70,70,fill="red")
        self.bloc.place(x=252,y=252)

        self.dice=Button(self.f,height=3,width=6,text="START\nGAME",command= self.gen)
        self.dice.place(x=300,y=295)

    count=0
    sixc=0
    sixc2=0
    sixc3=0
    sixc4=0
    siyc=0
    siyc2=0
    siyc3=0
    siyc4=0
    fc1=0
    fc2=0
    fc3=0
    fc4=0
    fc5=0
    fc6=0
    fc7=0
    fc8=0
    prevn=0
    prevn2=0
    prevn3=0
    prevn4=0
    prevn5=0
    prevn6=0
    prevn7=0
    prevn8=0
    dicet=0
    ty=0
    tr=0
    tt=0

    def openy(self,yval):

        if yval==1 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.yt1.destroy()
            self.yto=1
            self.prevn=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.sixc=0
            self.fc1=0
            self.moveyel()
        elif yval==2 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.yt2.destroy()
            self.yto=2
            self.prevn2=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.sixc2=0
            self.fc2=0
            self.moveyel()
        elif yval==3 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.yt3.destroy()
            self.yto=3
            self.prevn3=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.sixc3=0
            self.fc3=0
            self.moveyel()
        elif yval==4 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.yt4.destroy()
            self.yto=4
            self.prevn4=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.sixc4=0
            self.fc4=0
            self.moveyel()
        elif yval==5 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.rt1.destroy()
            self.yto=5
            self.prevn5=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.siyc=0
            self.fc5=0
            self.movered()
        elif yval==6 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.rt2.destroy()
            self.yto=6
            self.prevn6=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.siyc2=0
            self.fc6=0
            self.movered()
        elif yval==7 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.rt3.destroy()
            self.yto=7
            self.prevn7=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.siyc3=0
            self.fc7=0
            self.movered()
        elif yval==8 and self.dicet==1 and self.n==6 and self.nomovey==1:
            self.rt4.destroy()
            self.yto=8
            self.prevn8=0     #initializing these 3 to 0 because after clicking on tokken after its kill, it can start its game completely from beginning
            self.siyc4=0
            self.fc8=0
            self.movered()

        self.dicet=0    #dice-tokken-opening function
        self.nomovey=0
        self.rett()
    


    turn=0
    def tokturn(self):
        if self.turn==0:
            self.c3["bg"]="light goldenrod yellow"
            self.bloc.itemconfig(self.ye,fill="light goldenrod yellow")
        if self.turn==1:
            self.c1["bg"]="salmon1"
            self.bloc.itemconfig(self.rd,fill="salmon1")
    def rett(self):
        self.c3["bg"]="yellow"
        self.bloc.itemconfig(self.ye,fill="yellow")
        self.c1["bg"]="red"
        self.bloc.itemconfig(self.rd,fill="red")
        if self.turn==1:
            self.turn=0
        else:
            self.turn=1
    def gen(self):
        self.n=random.randint(1,6)
        self.dicet=1
        
        self.tokturn()
        self.tt=0


        if self.n==1:
            self.dice["text"]="●"
            

        if self.n==2:
            self.dice["text"]="●\n●"
            
            

        if self.n==3:
            self.dice["text"]="●\n●\n●"
           
            

        if self.n==4:

            self.dice["text"]="● ●\n● ●"
            
            

        if self.n==5:
            self.dice["text"]="● ●\n●\n● ●"
            
            

        if self.n==6:
            self.dice["text"]="● ●\n● ●\n● ●"
            self.count+=1
            self.nomovey=1
            


    flag1=0
    flag2=0
    flag3=0
    flag4=0

    fsx=0
    fsx2=0
    fsx3=0
    fsx4=0
    fsy=0
    fsy2=0
    fsy3=0
    fsy4=0
    box=0
    box2=0
    box3=0
    box4=0
    box5=0
    box6=0
    box7=0
    box8=0
    dne1=0
    dne2=0
    lasty=0
    lastr=0
    lastmove=0
    pos1=0
    pos2=0
    pos3=0
    pos4=0
    pos5=0
    pos6=0
    pos7=0
    pos8=0
    yw=0
    rw=0
    

    def kill(self):
        if self.lasty==1 or self.lasty==2 or self.lasty==3 or self.lasty==4:
            if self.lastmove==5 and self.pos1==self.pos5 and self.pos1!=1 and self.pos1!=9 and self.pos1!=14 and self.pos1!=22 and self.pos1!=27 and self.pos1!=35 and self.pos1!=40 and self.pos1!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y1.destroy()
                self.yt1=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(1))     #button 1
                self.yt1.place(x=72,y=72)
            elif self.lastmove==5 and self.pos2==self.pos5 and self.pos2!=1 and self.pos2!=9 and self.pos2!=14 and self.pos2!=22 and self.pos2!=27 and self.pos2!=35 and self.pos2!=40 and self.pos2!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y2.destroy()
                self.yt2=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(2))     #button 2
                self.yt2.place(x=152,y=72)
            elif self.lastmove==5 and self.pos3==self.pos5 and self.pos3!=1 and self.pos3!=9 and self.pos3!=14 and self.pos3!=22 and self.pos3!=27 and self.pos3!=35 and self.pos3!=40 and self.pos3!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y3.destroy()
                self.yt3=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(3))        #button 3
                self.yt3.place(x=72,y=152)
            elif self.lastmove==5 and self.pos4==self.pos5 and self.pos4!=1 and self.pos4!=9 and self.pos4!=14 and self.pos4!=22 and self.pos4!=27 and self.pos4!=35 and self.pos4!=40 and self.pos4!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y4.destroy()
                self.yt4=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(4))           #button 4
                self.yt4.place(x=152,y=152)
            elif self.lastmove==6 and self.pos1==self.pos6 and self.pos1!=1 and self.pos1!=9 and self.pos1!=14 and self.pos1!=22 and self.pos1!=27 and self.pos1!=35 and self.pos1!=40 and self.pos1!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y1.destroy()
                self.yt1=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(1))     #button 1
                self.yt1.place(x=72,y=72)
            elif self.lastmove==6 and self.pos2==self.pos6 and self.pos2!=1 and self.pos2!=9 and self.pos2!=14 and self.pos2!=22 and self.pos2!=27 and self.pos2!=35 and self.pos2!=40 and self.pos2!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y2.destroy()
                self.yt2=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(2))     #button 2
                self.yt2.place(x=152,y=72)
            elif self.lastmove==6 and self.pos3==self.pos6 and self.pos3!=1 and self.pos3!=9 and self.pos3!=14 and self.pos3!=22 and self.pos3!=27 and self.pos3!=35 and self.pos3!=40 and self.pos3!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y3.destroy()
                self.yt3=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(3))        #button 3
                self.yt3.place(x=72,y=152)
            elif self.lastmove==6 and self.pos4==self.pos6 and self.pos4!=1 and self.pos4!=9 and self.pos4!=14 and self.pos4!=22 and self.pos4!=27 and self.pos4!=35 and self.pos4!=40 and self.pos4!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y4.destroy()
                self.yt4=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(4))           #button 4
                self.yt4.place(x=152,y=152)
            elif self.lastmove==7 and self.pos1==self.pos7 and self.pos1!=1 and self.pos1!=9 and self.pos1!=14 and self.pos1!=22 and self.pos1!=27 and self.pos1!=35 and self.pos1!=40 and self.pos1!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y1.destroy()
                self.yt1=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(1))     #button 1
                self.yt1.place(x=72,y=72)
            elif self.lastmove==7 and self.pos2==self.pos7 and self.pos2!=1 and self.pos2!=9 and self.pos2!=14 and self.pos2!=22 and self.pos2!=27 and self.pos2!=35 and self.pos2!=40 and self.pos2!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y2.destroy()
                self.yt2=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(2))     #button 2
                self.yt2.place(x=152,y=72)
            elif self.lastmove==7 and self.pos3==self.pos7 and self.pos3!=1 and self.pos3!=9 and self.pos3!=14 and self.pos3!=22 and self.pos3!=27 and self.pos3!=35 and self.pos3!=40 and self.pos3!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y3.destroy()
                self.yt3=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(3))        #button 3
                self.yt3.place(x=72,y=152)
            elif self.lastmove==7 and self.pos4==self.pos7 and self.pos4!=1 and self.pos4!=9 and self.pos4!=14 and self.pos4!=22 and self.pos4!=27 and self.pos4!=35 and self.pos4!=40 and self.pos4!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y4.destroy()
                self.yt4=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(4))           #button 4
                self.yt4.place(x=152,y=152)
            elif self.lastmove==8 and self.pos1==self.pos8 and self.pos1!=1 and self.pos1!=9 and self.pos1!=14 and self.pos1!=22 and self.pos1!=27 and self.pos1!=35 and self.pos1!=40 and self.pos1!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y1.destroy()
                self.yt1=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(1))     #button 1
                self.yt1.place(x=72,y=72)
            elif self.lastmove==8 and self.pos2==self.pos8 and self.pos2!=1 and self.pos2!=9 and self.pos2!=14 and self.pos2!=22 and self.pos2!=27 and self.pos2!=35 and self.pos2!=40 and self.pos2!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y2.destroy()
                self.yt2=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(2))     #button 2
                self.yt2.place(x=152,y=72)
            elif self.lastmove==8 and self.pos3==self.pos8 and self.pos3!=1 and self.pos3!=9 and self.pos3!=14 and self.pos3!=22 and self.pos3!=27 and self.pos3!=35 and self.pos3!=40 and self.pos3!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y3.destroy()
                self.yt3=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(3))        #button 3
                self.yt3.place(x=72,y=152)
            elif self.lastmove==8 and self.pos4==self.pos8 and self.pos4!=1 and self.pos4!=9 and self.pos4!=14 and self.pos4!=22 and self.pos4!=27 and self.pos4!=35 and self.pos4!=40 and self.pos4!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="yellow")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('YELLOW PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.y4.destroy()
                self.yt4=Button(self.c3,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda: self.openy(4))           #button 4
                self.yt4.place(x=152,y=152)
        if self.lastr==1 or self.lastr==2 or self.lastr==3 or self.lastr==4:
            if self.lastmove==1 and self.pos5==self.pos1 and self.pos5!=1 and self.pos5!=9 and self.pos5!=14 and self.pos5!=22 and self.pos5!=27 and self.pos5!=35 and self.pos5!=40 and self.pos5!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r1.destroy()
                self.rt1=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(5))     #button 1
                self.rt1.place(x=72,y=72)
            elif self.lastmove==1 and self.pos6==self.pos1 and self.pos6!=1 and self.pos6!=9 and self.pos6!=14 and self.pos6!=22 and self.pos6!=27 and self.pos6!=35 and self.pos6!=40 and self.pos6!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r2.destroy()
                self.rt2=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(6))     #button 2
                self.rt2.place(x=152,y=72)
            elif self.lastmove==1 and self.pos7==self.pos1 and self.pos7!=1 and self.pos7!=9 and self.pos7!=14 and self.pos7!=22 and self.pos7!=27 and self.pos7!=35 and self.pos7!=40 and self.pos7!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r3.destroy()
                self.rt3=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(7))        #button 3
                self.rt3.place(x=72,y=152)
            elif self.lastmove==1 and self.pos8==self.pos1 and self.pos8!=1 and self.pos8!=9 and self.pos8!=14 and self.pos8!=22 and self.pos8!=27 and self.pos8!=35 and self.pos8!=40 and self.pos8!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r4.destroy()
                self.rt4=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(8))           #button 4
                self.rt4.place(x=152,y=152)
            elif self.lastmove==2 and self.pos5==self.pos2 and self.pos5!=1 and self.pos5!=9 and self.pos5!=14 and self.pos5!=22 and self.pos5!=27 and self.pos5!=35 and self.pos5!=40 and self.pos5!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r1.destroy()
                self.rt1=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(5))     #button 1
                self.rt1.place(x=72,y=72)
            elif self.lastmove==2 and self.pos6==self.pos2 and self.pos6!=1 and self.pos6!=9 and self.pos6!=14 and self.pos6!=22 and self.pos6!=27 and self.pos6!=35 and self.pos6!=40 and self.pos6!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r2.destroy()
                self.rt2=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(6))     #button 2
                self.rt2.place(x=152,y=72)
            elif self.lastmove==2 and self.pos7==self.pos2 and self.pos7!=1 and self.pos7!=9 and self.pos7!=14 and self.pos7!=22 and self.pos7!=27 and self.pos7!=35 and self.pos7!=40 and self.pos7!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r3.destroy()
                self.rt3=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(7))        #button 3
                self.rt3.place(x=72,y=152)
            elif self.lastmove==2 and self.pos8==self.pos2 and self.pos8!=1 and self.pos8!=9 and self.pos8!=14 and self.pos8!=22 and self.pos8!=27 and self.pos8!=35 and self.pos8!=40 and self.pos8!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r4.destroy()
                self.rt4=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(8))           #button 4
                self.rt4.place(x=152,y=152)
            elif self.lastmove==3 and self.pos5==self.pos3 and self.pos5!=1 and self.pos5!=9 and self.pos5!=14 and self.pos5!=22 and self.pos5!=27 and self.pos5!=35 and self.pos5!=40 and self.pos5!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r1.destroy()
                self.rt1=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(5))     #button 1
                self.rt1.place(x=72,y=72)
            elif self.lastmove==3 and self.pos6==self.pos3 and self.pos6!=1 and self.pos6!=9 and self.pos6!=14 and self.pos6!=22 and self.pos6!=27 and self.pos6!=35 and self.pos6!=40 and self.pos6!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r2.destroy()
                self.rt2=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(6))     #button 2
                self.rt2.place(x=152,y=72)
            elif self.lastmove==3 and self.pos7==self.pos3 and self.pos7!=1 and self.pos7!=9 and self.pos7!=14 and self.pos7!=22 and self.pos7!=27 and self.pos7!=35 and self.pos7!=40 and self.pos7!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r3.destroy()
                self.rt3=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(7))        #button 3
                self.rt3.place(x=72,y=152)
            elif self.lastmove==3 and self.pos8==self.pos3 and self.pos8!=1 and self.pos8!=9 and self.pos8!=14 and self.pos8!=22 and self.pos8!=27 and self.pos8!=35 and self.pos8!=40 and self.pos8!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r4.destroy()
                self.rt4=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(8))           #button 4
                self.rt4.place(x=152,y=152)
            elif self.lastmove==4 and self.pos5==self.pos4 and self.pos5!=1 and self.pos5!=9 and self.pos5!=14 and self.pos5!=22 and self.pos5!=27 and self.pos5!=35 and self.pos5!=40 and self.pos5!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r1.destroy()
                self.rt1=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(5))     #button 1
                self.rt1.place(x=72,y=72)
            elif self.lastmove==4 and self.pos6==self.pos4 and self.pos6!=1 and self.pos6!=9 and self.pos6!=14 and self.pos6!=22 and self.pos6!=27 and self.pos6!=35 and self.pos6!=40 and self.pos6!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r2.destroy()
                self.rt2=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(6))     #button 2
                self.rt2.place(x=152,y=72)
            elif self.lastmove==4 and self.pos7==self.pos4 and self.pos7!=1 and self.pos7!=9 and self.pos7!=14 and self.pos7!=22 and self.pos7!=27 and self.pos7!=35 and self.pos7!=40 and self.pos7!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r3.destroy()
                self.rt3=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(7))        #button 3
                self.rt3.place(x=72,y=152)
            elif self.lastmove==4 and self.pos8==self.pos4 and self.pos8!=1 and self.pos8!=9 and self.pos8!=14 and self.pos8!=22 and self.pos8!=27 and self.pos8!=35 and self.pos8!=40 and self.pos8!=48:
                ab=Tk()
                w=Frame(ab,height=100,width=300,bg="red")
                l1=Label(w,text="Your tokken is killed!")
                b1=Button(w,height=2,width=4,text="OK",command=ab.destroy)
                ab.title('RED PLAYER')
                w.pack()
                l1.pack()
                b1.pack()
                self.r4.destroy()
                self.rt4=Button(self.c1,height=1,width=2,text="X",bg="salmon1",command=lambda: self.openy(8))           #button 4
                self.rt4.place(x=152,y=152)
        
            


    
    def abx1(self,vv):       #individual moving of yellow tokken
        if vv==1:
            self.yto=1
            self.lasty=1
            
        elif vv==2:
            self.yto=2
            self.lasty=2
            
        elif vv==3:
            self.yto=3
            self.lasty=3
            
        elif vv==4:
            self.yto=4
            self.lasty=4
            
        elif vv==5:
            self.yto=5
            self.lastr=1
            
        elif vv==6:
            self.yto=6
            self.lastr=2
            
        elif vv==7:
            self.yto=7
            self.lastr=3
            
        elif vv==8:
            self.yto=8
            self.lastr=4
    def win(self):
        if self.yw==4:
            nn=Tk()
            a=Canvas(nn,height=600,width=600,bg="yellow")
            a.pack()
            l1=Label(a,text="CONGRATULATIONS! PLAYER 1 WINS.",font=14)
            l1.pack()
            nn.title("YELLOW WINS!")
            nn.mainloop()
        elif self.rw==4:
            nn=Tk()
            a=Canvas(nn,height=600,width=600,bg="red")
            a.pack()
            l1=Label(a,text="CONGRATULATIONS! PLAYER 2 WINS.",font=14)
            l1.pack()
            nn.title("RED WINS!")


    
    def moveyel(self):
        self.rett()
        self.win()
        if self.count>=1 and self.yto==1 and self.tt<1:    #opening tokken 1
            
            self.lastmove=1
            if self.n==6 and self.sixc==0 and self.fc1==0:
                self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                self.y1.place(x=262,y=575)
                self.sixc+=1
                self.pos1=1
                
            elif self.n==1 and self.fc1==0 and self.yto==1:
                self.y1.place(x=262,y=575-42)
                self.prevn=1
                self.fc1+=1
                self.pos1=2
            elif self.n==2 and self.fc1==0 and self.yto==1:
                self.y1.place(x=262,y=575-84)
                self.prevn=2
                self.fc1+=1
                self.pos1=3
    
            elif self.n==3 and self.fc1==0 and self.yto==1:
                self.y1.place(x=262,y=575-126)
                self.prevn=3
                self.fc1+=1
                self.pos1=4
                
            elif self.n==4 and self.fc1==0 and self.yto==1:
                self.y1.place(x=262,y=575-168)
                self.prevn=4
                self.fc1+=1
                self.pos1=5
                
            elif self.n==5 and self.fc1==0 and self.yto==1:
                self.y1.place(x=218,y=362)
                self.prevn=5
                self.fc1+=1
                self.pos1=6
                
            elif self.n==6 and self.fc1==0 and self.sixc==1 and self.yto==1:
                self.fc1+=1
                self.fsx+=1
                self.sixc+=1
                self.y1.place(x=218-40,y=362)
                self.prevn=6
                self.pos1=7

            elif self.fc1>=1 and self.yto==1:                  #moving of tokken 1
                self.box=self.prevn+self.n
                if self.box==2:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=492)
                    self.prevn=2
                    self.pos1=3
                elif self.box==3:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=449)
                    self.prevn=3
                    self.pos1=4
                elif self.box==4:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=406)
                    self.prevn=4
                    self.pos1=5
                elif self.box==5:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=218,y=362)
                    self.prevn=5
                    self.pos1=6
                elif self.box==6:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=178,y=362)
                    self.prevn=6
                    self.pos1=7
                elif self.box==7:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=138,y=362)
                    self.prevn=7
                    self.pos1=8
                elif self.box==8:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=98,y=362)
                    self.prevn=8
                    self.pos1=9
                elif self.box==9:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=52,y=362)
                    self.prevn=9
                    self.pos1=10
                elif self.box==10:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=10,y=362)
                    self.prevn=10
                    self.pos1=11
                elif self.box==11:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=10,y=304)
                    self.prevn=11
                    self.pos1=12
                elif self.box==12:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=10,y=262)
                    self.prevn=12
                    self.pos1=13
                elif self.box==13:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=50,y=262)
                    self.prevn=13
                    self.pos1=14
                elif self.box==14:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=98,y=262)
                    self.prevn=14
                    self.pos1=15
                elif self.box==15:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=138,y=262)
                    self.prevn=15
                    self.pos1=16
                elif self.box==16:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=178,y=262)
                    self.prevn=16
                    self.pos1=17
                elif self.box==17:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=218,y=262)
                    self.prevn=17
                    self.pos1=18
                elif self.box==18:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=221)
                    self.prevn=18
                    self.pos1=19
                elif self.box==19:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=179)
                    self.prevn=19
                    self.pos1=20
                elif self.box==20:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=137)
                    self.prevn=20
                    self.pos1=21
                elif self.box==21:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=95)
                    self.prevn=21
                    self.pos1=22
                elif self.box==22:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=52)
                    self.prevn=22
                    self.pos1=23
                elif self.box==23:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=262,y=10)
                    self.prevn=23
                    self.pos1=24
                elif self.box==24:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=304,y=10)
                    self.prevn=24
                    self.pos1=25
                elif self.box==25:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=10)
                    self.prevn=25
                    self.pos1=26
                elif self.box==26:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=52)
                    self.prevn=26
                    self.pos1=27
                elif self.box==27:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=95)
                    self.prevn=27
                    self.pos1=28
                elif self.box==28:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=137)
                    self.prevn=28
                    self.pos1=29
                elif self.box==29:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=179)
                    self.prevn=29
                    self.pos1=30
                elif self.box==30:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=221)
                    self.prevn=30
                    self.pos1=31
                elif self.box==31:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=407,y=262)
                    self.prevn=31
                    self.pos1=32
                elif self.box==32:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=449,y=262)
                    self.prevn=32
                    self.pos1=33
                elif self.box==33:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=491,y=262)
                    self.prevn=33
                    self.pos1=34
                elif self.box==34:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=533,y=262)
                    self.prevn=34
                    self.pos1=35
                elif self.box==35:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=575,y=262)
                    self.prevn=35
                    self.pos1=36
                elif self.box==36:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=617,y=262)
                    self.prevn=36
                    self.pos1=37
                elif self.box==37:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=617,y=304)
                    self.prevn=37
                    self.pos1=38
                elif self.box==38:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=617,y=362)
                    self.prevn=38
                    self.pos1=39
                elif self.box==39:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=575,y=362)
                    self.prevn=39
                    self.pos1=40
                elif self.box==40:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=533,y=362)
                    self.prevn=40
                    self.pos1=41
                elif self.box==41:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=491,y=362)
                    self.prevn=41
                    self.pos1=42
                elif self.box==42:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=449,y=362)
                    self.prevn=42
                    self.pos1=43
                elif self.box==43:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=407,y=362)
                    self.prevn=43
                    self.pos1=44
                elif self.box==44:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=406)
                    self.prevn=44
                    self.pos1=45
                elif self.box==45:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=449)
                    self.prevn=45
                    self.pos1=46
                elif self.box==46:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=492)
                    self.prevn=46
                    self.pos1=47
                elif self.box==47:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=534)
                    self.prevn=47
                    self.pos1=48
                elif self.box==48:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=576)
                    self.prevn=48
                    self.pos1=49
                elif self.box==49:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=364,y=618)
                    self.prevn=49
                    self.pos1=50
                elif self.box==50:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=314,y=618)
                    self.prevn=50
                    self.pos1=51
                elif self.box==51:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=314,y=576)
                    self.prevn=51
                    self.pos1=52
                elif self.box==52:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=314,y=534)
                    self.prevn=52
                    self.pos1=53
                elif self.box==53:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=314,y=492)
                    self.prevn=53
                    self.pos1=54
                elif self.box==54:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=314,y=449)
                    self.prevn=54
                    self.pos1=55
                elif self.box==55:
                    self.y1.destroy()
                    self.y1=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(1),self.moveyel()])
                    self.y1.place(x=314,y=406)
                    self.prevn=55
                    self.pos1=56
                elif self.box==56:
                    self.y1.destroy()
                    self.hy1=Button(self.f,height=1,width=1,text="X",bg="light goldenrod yellow")
                    self.hy1.place(x=287,y=362)
                    self.yw+=1
            
            self.kill()

        if self.count>=1 and self.yto==2 and self.tt<1:                 #opening tokken 2
            
            self.lastmove=2
            if self.n==6 and self.sixc2==0 and self.fc2==0:
                self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                self.y2.place(x=262,y=575)
                self.sixc2+=1
                self.pos2=1
                
            elif self.n==1 and self.fc2==0 and self.yto==2:
                self.y2.place(x=262,y=575-42)
                self.prevn2=1
                self.fc2+=1
                self.pos2=2
            elif self.n==2 and self.fc2==0 and self.yto==2:
                self.y2.place(x=262,y=575-84)
                self.prevn2=2
                self.fc2+=1
                self.pos2=3
    
            elif self.n==3 and self.fc2==0 and self.yto==2:
                self.y2.place(x=262,y=575-126)
                self.prevn2=3
                self.fc2+=1
                self.pos2=4
                
            elif self.n==4 and self.fc2==0 and self.yto==2:
                self.y2.place(x=262,y=575-168)
                self.prevn2=4
                self.fc2+=1
                self.pos2=5
                
            elif self.n==5 and self.fc2==0 and self.yto==2:
                self.y2.place(x=218,y=362)
                self.prevn2=5
                self.fc2+=1
                self.pos2=6
                
            elif self.n==6 and self.fc2==0 and self.sixc2==1 and self.yto==2:
                self.fc2+=1
                self.fsx2+=1
                self.sixc2+=1
                self.y2.place(x=218-40,y=362)
                self.prevn2=6
                self.pos2=7

            elif self.fc2>=1 and self.yto==2:                  #moving of tokken 2
                self.box2=self.prevn2+self.n
                if self.box2==2:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=492)
                    self.prevn2=2
                    self.pos2=3
                elif self.box2==3:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=449)
                    self.prevn2=3
                    self.pos2=4
                elif self.box2==4:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=406)
                    self.prevn2=4
                    self.pos2=5
                elif self.box2==5:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=218,y=362)
                    self.prevn2=5
                    self.pos2=6
                elif self.box2==6:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=178,y=362)
                    self.prevn2=6
                    self.pos2=7
                elif self.box2==7:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=138,y=362)
                    self.prevn2=7
                    self.pos2=8
                elif self.box2==8:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=98,y=362)
                    self.prevn2=8
                    self.pos2=9
                elif self.box2==9:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=52,y=362)
                    self.prevn2=9
                    self.pos2=10
                elif self.box2==10:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=10,y=362)
                    self.prevn2=10
                    self.pos2=11
                elif self.box2==11:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=10,y=304)
                    self.prevn2=11
                    self.pos2=12
                elif self.box2==12:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=10,y=262)
                    self.prevn2=12
                    self.pos2=13
                elif self.box2==13:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=50,y=262)
                    self.prevn2=13
                    self.pos2=14
                elif self.box2==14:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=98,y=262)
                    self.prevn2=14
                    self.pos2=15
                elif self.box2==15:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=138,y=262)
                    self.prevn2=15
                    self.pos2=16
                elif self.box2==16:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=178,y=262)
                    self.prevn2=16
                    self.pos2=17
                elif self.box2==17:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=218,y=262)
                    self.prevn2=17
                    self.pos2=18
                elif self.box2==18:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=221)
                    self.prevn2=18
                    self.pos2=19
                elif self.box2==19:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=179)
                    self.prevn2=19
                    self.pos2=20
                elif self.box2==20:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=137)
                    self.prevn2=20
                    self.pos2=21
                elif self.box2==21:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=95)
                    self.prevn2=21
                    self.pos2=22
                elif self.box2==22:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=52)
                    self.prevn2=22
                    self.pos2=23
                elif self.box2==23:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=262,y=10)
                    self.prevn2=23
                    self.pos2=24
                elif self.box2==24:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=304,y=10)
                    self.prevn2=24
                    self.pos2=25
                elif self.box2==25:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=10)
                    self.prevn2=25
                    self.pos2=26
                elif self.box2==26:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=52)
                    self.prevn2=26
                    self.pos2=27
                elif self.box2==27:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=95)
                    self.prevn2=27
                    self.pos2=28
                elif self.box2==28:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=137)
                    self.prevn2=28
                    self.pos2=29
                elif self.box2==29:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=179)
                    self.prevn2=29
                    self.pos2=30
                elif self.box2==30:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=221)
                    self.prevn2=30
                    self.pos2=31
                elif self.box2==31:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=407,y=262)
                    self.prevn2=31
                    self.pos2=32
                elif self.box2==32:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=449,y=262)
                    self.prevn2=32
                    self.pos2=33
                elif self.box2==33:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=491,y=262)
                    self.prevn2=33
                    self.pos2=34
                elif self.box2==34:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=533,y=262)
                    self.prevn2=34
                    self.pos2=35
                elif self.box2==35:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=575,y=262)
                    self.prevn2=35
                    self.pos2=36
                elif self.box2==36:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=617,y=262)
                    self.prevn2=36
                    self.pos2=37
                elif self.box2==37:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=617,y=304)
                    self.prevn2=37
                    self.pos2=38
                elif self.box2==38:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=617,y=362)
                    self.prevn2=38
                    self.pos2=39
                elif self.box2==39:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=575,y=362)
                    self.prevn2=39
                    self.pos2=40
                elif self.box2==40:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=533,y=362)
                    self.prevn2=40
                    self.pos2=41
                elif self.box2==41:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=491,y=362)
                    self.prevn2=41
                    self.pos2=42
                elif self.box2==42:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=449,y=362)
                    self.prevn2=42
                    self.pos2=43
                elif self.box2==43:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=407,y=362)
                    self.prevn2=43
                    self.pos2=44
                elif self.box2==44:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=406)
                    self.prevn2=44
                    self.pos2=45
                elif self.box2==45:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=449)
                    self.prevn2=45
                    self.pos2=46
                elif self.box2==46:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=492)
                    self.prevn2=46
                    self.pos2=47
                elif self.box2==47:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=534)
                    self.prevn2=47
                    self.pos2=48
                elif self.box2==48:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=576)
                    self.prevn2=48
                    self.pos2=49
                elif self.box2==49:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=364,y=618)
                    self.prevn2=49
                    self.pos2=50
                elif self.box2==50:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=314,y=618)
                    self.prevn2=50
                    self.pos2=51
                elif self.box2==51:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=314,y=576)
                    self.prevn2=51
                    self.pos2=52
                elif self.box2==52:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=314,y=534)
                    self.prevn2=52
                    self.pos2=53
                elif self.box2==53:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=314,y=492)
                    self.prevn2=54
                elif self.box2==54:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=314,y=449)
                    self.prevn2=55
                elif self.box2==55:
                    self.y2.destroy()
                    self.y2=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(2),self.moveyel()])
                    self.y2.place(x=314,y=406)
                    self.prevn2=55
                    self.pos2=56
                elif self.box2==56:
                    self.y2.destroy()
                    self.hy2=Button(self.f,height=1,width=1,text="X",bg="light goldenrod yellow")
                    self.hy2.place(x=305,y=362)
                    self.yw+=1
            
            self.kill()

        if self.count>=1 and self.yto==3 and self.tt<1:                 #opening tokken 3
            
            self.lastmove=3
            if self.n==6 and self.sixc3==0 and self.fc3==0:
                self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                self.y3.place(x=262,y=575)
                self.sixc3+=1
                self.pos3=1
            elif self.n==1 and self.fc3==0 and self.yto==3:
                self.y3.place(x=262,y=575-42)
                self.prevn3=1
                self.fc3+=1
                self.pos3=2
            elif self.n==2 and self.fc3==0 and self.yto==3:
                self.y3.place(x=262,y=575-84)
                self.prevn3=2
                self.fc3+=1
                self.pos3=3
    
            elif self.n==3 and self.fc3==0 and self.yto==3:
                self.y3.place(x=262,y=575-126)
                self.prevn3=3
                self.fc3+=1
                self.pos3=4
                
            elif self.n==4 and self.fc3==0 and self.yto==3:
                self.y3.place(x=262,y=575-168)
                self.prevn3=4
                self.fc3+=1
                self.pos3=5
                
            elif self.n==5 and self.fc3==0 and self.yto==3:
                self.y3.place(x=218,y=362)
                self.prevn3=5
                self.fc3+=1
                self.pos3=6
                
            elif self.n==6 and self.fc3==0 and self.sixc3==1 and self.yto==3:
                self.fc3+=1
                self.fsx3+=1
                self.sixc3+=1
                self.y3.place(x=218-40,y=362)
                self.prevn3=6
                self.pos3=7

            elif self.fc3>=1 and self.yto==3:                  #moving of tokken 3
                self.box3=self.prevn3+self.n
                if self.box3==2:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=492)
                    self.prevn3=2
                    self.pos3=3
                elif self.box3==3:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=449)
                    self.prevn3=3
                    self.pos3=4
                elif self.box3==4:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=406)
                    self.prevn3=4
                    self.pos3=5
                elif self.box3==5:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=218,y=362)
                    self.prevn3=5
                    self.pos3=6
                elif self.box3==6:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=178,y=362)
                    self.prevn3=6
                    self.pos3=7
                elif self.box3==7:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=138,y=362)
                    self.prevn3=7
                    self.pos3=8
                elif self.box3==8:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=98,y=362)
                    self.prevn3=8
                    self.pos3=9
                elif self.box3==9:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=52,y=362)
                    self.prevn3=9
                    self.pos3=10
                elif self.box3==10:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=10,y=362)
                    self.prevn3=10
                    self.pos3=11
                elif self.box3==11:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=10,y=304)
                    self.prevn3=11
                    self.pos3=12
                elif self.box3==12:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=10,y=262)
                    self.prevn3=12
                    self.pos3=13
                elif self.box3==13:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=50,y=262)
                    self.prevn3=13
                    self.pos3=14
                elif self.box3==14:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=98,y=262)
                    self.prevn3=14
                    self.pos3=15
                elif self.box3==15:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=138,y=262)
                    self.prevn3=15
                    self.pos3=16
                elif self.box3==16:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=178,y=262)
                    self.prevn3=16
                    self.pos3=17
                elif self.box3==17:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=218,y=262)
                    self.prevn3=17
                    self.pos3=18
                elif self.box3==18:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=221)
                    self.prevn3=18
                    self.pos3=19
                elif self.box3==19:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=179)
                    self.prevn3=19
                    self.pos3=20
                elif self.box3==20:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=137)
                    self.prevn3=20
                    self.pos3=21
                elif self.box3==21:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=95)
                    self.prevn3=21
                    self.pos3=22
                elif self.box3==22:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=52)
                    self.prevn3=22
                    self.pos3=23
                elif self.box3==23:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=262,y=10)
                    self.prevn3=23
                    self.pos3=24
                elif self.box3==24:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=304,y=10)
                    self.prevn3=24
                    self.pos3=25
                elif self.box3==25:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=10)
                    self.prevn3=25
                    self.pos3=26
                elif self.box3==26:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=52)
                    self.prevn3=26
                    self.pos3=27
                elif self.box3==27:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=95)
                    self.prevn3=27
                    self.pos3=28
                elif self.box3==28:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=137)
                    self.prevn3=28
                    self.pos3=29
                elif self.box3==29:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=179)
                    self.prevn3=29
                    self.pos3=30
                elif self.box3==30:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=221)
                    self.prevn3=30
                    self.pos3=31
                elif self.box3==31:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=407,y=262)
                    self.prevn3=31
                    self.pos3=32
                elif self.box3==32:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=449,y=262)
                    self.prevn3=32
                    self.pos3=33
                elif self.box3==33:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=491,y=262)
                    self.prevn3=33
                    self.pos3=34
                elif self.box3==34:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=533,y=262)
                    self.prevn3=34
                    self.pos3=35
                elif self.box3==35:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=575,y=262)
                    self.prevn3=35
                    self.pos3=36
                elif self.box3==36:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=617,y=262)
                    self.prevn3=36
                    self.pos3=37
                elif self.box3==37:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=617,y=304)
                    self.prevn3=37
                    self.pos3=38
                elif self.box3==38:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=617,y=362)
                    self.prevn3=38
                    self.pos3=39
                elif self.box3==39:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=575,y=362)
                    self.prevn3=39
                    self.pos3=40
                elif self.box3==40:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=533,y=362)
                    self.prevn3=40
                    self.pos3=41
                elif self.box3==41:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=491,y=362)
                    self.prevn3=41
                    self.pos3=42
                elif self.box3==42:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=449,y=362)
                    self.prevn3=42
                    self.pos3=43
                elif self.box3==43:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=407,y=362)
                    self.prevn3=43
                    self.pos3=44
                elif self.box3==44:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=406)
                    self.prevn3=44
                    self.pos3=45
                elif self.box3==45:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=449)
                    self.prevn3=45
                    self.pos3=46
                elif self.box3==46:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=492)
                    self.prevn3=46
                    self.pos3=47
                elif self.box3==47:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=534)
                    self.prevn3=47
                    self.pos3=48
                elif self.box3==48:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=576)
                    self.prevn3=48
                    self.pos3=49
                elif self.box3==49:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=364,y=618)
                    self.prevn3=49
                    self.pos3=50
                elif self.box3==50:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=314,y=618)
                    self.prevn3=50
                    self.pos3=51
                elif self.box3==51:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=314,y=576)
                    self.prevn3=51
                    self.pos3=52
                elif self.box3==52:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=314,y=534)
                    self.prevn3=52
                    self.pos3=53
                elif self.box3==53:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=314,y=492)
                    self.prevn3=53
                    self.pos3=54
                elif self.box3==54:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=314,y=449)
                    self.prevn3=54
                    self.pos3=55
                elif self.box3==55:
                    self.y3.destroy()
                    self.y3=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(3),self.moveyel()])
                    self.y3.place(x=314,y=406)
                    self.prevn3=55
                    self.pos3=56
                elif self.box3==56:
                    self.y3.destroy()
                    self.hy3=Button(self.f,height=1,width=1,text="X",bg="light goldenrod yellow")
                    self.hy3.place(x=323,y=362)
                    self.yw+=1
            
            self.kill()


        if self.count>=1 and self.yto==4 and self.tt<1:                 #opening tokken 4
            
            self.lastmove=4
            if self.n==6 and self.sixc4==0 and self.fc4==0:
                self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                self.y4.place(x=262,y=575)
                self.sixc4+=1
                self.pos4=1
            elif self.n==1 and self.fc4==0 and self.yto==4:
                self.y4.place(x=262,y=575-42)
                self.prevn4=1
                self.fc4+=1
                self.pos4=2
            elif self.n==2 and self.fc4==0 and self.yto==4:
                self.y4.place(x=262,y=575-84)
                self.prevn4=2
                self.fc4+=1
                self.pos4=3
    
            elif self.n==3 and self.fc4==0 and self.yto==4:
                self.y4.place(x=262,y=575-126)
                self.prevn4=3
                self.fc4+=1
                self.pos4=4
                
            elif self.n==4 and self.fc4==0 and self.yto==4:
                self.y4.place(x=262,y=575-168)
                self.prevn4=4
                self.fc4+=1
                self.pos4=5
                
            elif self.n==5 and self.fc4==0 and self.yto==4:
                self.y4.place(x=218,y=362)
                self.prevn4=5
                self.fc4+=1
                self.pos4=6
                
            elif self.n==6 and self.fc4==0 and self.sixc4==1 and self.yto==4:
                self.fc4+=1
                self.fsx4+=1
                self.sixc4+=1
                self.y4.place(x=218-40,y=362)
                self.prevn4=6
                self.pos4=7

            elif self.fc4>=1 and self.yto==4:                  #moving of tokken 4
                self.box4=self.prevn4+self.n
                if self.box4==2:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=492)
                    self.prevn4=2
                    self.pos4=3
                elif self.box4==3:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=449)
                    self.prevn4=3
                    self.pos4=4
                elif self.box4==4:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=406)
                    self.prevn4=4
                    self.pos4=5
                elif self.box4==5:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=218,y=362)
                    self.prevn4=5
                    self.pos4=6
                elif self.box4==6:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=178,y=362)
                    self.prevn4=6
                    self.pos4=7
                elif self.box4==7:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=138,y=362)
                    self.prevn4=7
                    self.pos4=8
                elif self.box4==8:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=98,y=362)
                    self.prevn4=8
                    self.pos4=9
                elif self.box4==9:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=52,y=362)
                    self.prevn4=9
                    self.pos4=10
                elif self.box4==10:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=10,y=362)
                    self.prevn4=10
                    self.pos4=11
                elif self.box4==11:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=10,y=304)
                    self.prevn4=11
                    self.pos4=12
                elif self.box4==12:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=10,y=262)
                    self.prevn4=12
                    self.pos4=13
                elif self.box4==13:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=50,y=262)
                    self.prevn4=13
                    self.pos4=14
                elif self.box4==14:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=98,y=262)
                    self.prevn4=14
                    self.pos4=15
                elif self.box4==15:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=138,y=262)
                    self.prevn4=15
                    self.pos4=16
                elif self.box4==16:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=178,y=262)
                    self.prevn4=16
                    self.pos4=17
                elif self.box4==17:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=218,y=262)
                    self.prevn4=17
                    self.pos4=18
                elif self.box4==18:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=221)
                    self.prevn4=18
                    self.pos4=19
                elif self.box4==19:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=179)
                    self.prevn4=19
                    self.pos4=20
                elif self.box4==20:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=137)
                    self.prevn4=20
                    self.pos4=21
                elif self.box4==21:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=95)
                    self.prevn4=21
                    self.pos4=22
                elif self.box4==22:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=52)
                    self.prevn4=22
                    self.pos4=23
                elif self.box4==23:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=262,y=10)
                    self.prevn4=23
                    self.pos4=24
                elif self.box4==24:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=304,y=10)
                    self.prevn4=24
                    self.pos4=25
                elif self.box4==25:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=10)
                    self.prevn4=25
                    self.pos4=26
                elif self.box4==26:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=52)
                    self.prevn4=26
                    self.pos4=27
                elif self.box4==27:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=95)
                    self.prevn4=27
                    self.pos4=28
                elif self.box4==28:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=137)
                    self.prevn4=28
                    self.pos4=29
                elif self.box4==29:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=179)
                    self.prevn4=29
                    self.pos4=30
                elif self.box4==30:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=221)
                    self.prevn4=30
                    self.pos4=31
                elif self.box4==31:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=407,y=262)
                    self.prevn4=31
                    self.pos4=32
                elif self.box4==32:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=449,y=262)
                    self.prevn4=32
                    self.pos4=33
                elif self.box4==33:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=491,y=262)
                    self.prevn4=33
                    self.pos4=34
                elif self.box4==34:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=533,y=262)
                    self.prevn4=34
                    self.pos4=35
                elif self.box4==35:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=575,y=262)
                    self.prevn4=35
                    self.pos4=36
                elif self.box4==36:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=617,y=262)
                    self.prevn4=36
                    self.pos4=37
                elif self.box4==37:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=617,y=304)
                    self.prevn4=37
                    self.pos4=38
                elif self.box4==38:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=617,y=362)
                    self.prevn4=38
                    self.pos4=39
                elif self.box4==39:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=575,y=362)
                    self.prevn4=39
                    self.pos4=40
                elif self.box4==40:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=533,y=362)
                    self.prevn4=40
                    self.pos4=41
                elif self.box4==41:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=491,y=362)
                    self.prevn4=41
                    self.pos4=42
                elif self.box4==42:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=449,y=362)
                    self.prevn4=42
                    self.pos4=43
                elif self.box4==43:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=407,y=362)
                    self.prevn4=43
                    self.pos4=44
                elif self.box4==44:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=406)
                    self.prevn4=44
                    self.pos4=45
                elif self.box4==45:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=449)
                    self.prevn4=45
                    self.pos4=46
                elif self.box4==46:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=492)
                    self.prevn4=46
                    self.pos4=47
                elif self.box4==47:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=534)
                    self.prevn4=47
                    self.pos4=48
                elif self.box4==48:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=576)
                    self.prevn4=48
                    self.pos4=49
                elif self.box4==49:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=364,y=618)
                    self.prevn4=49
                    self.pos4=50
                elif self.box4==50:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=314,y=618)
                    self.prevn4=50
                    self.pos4=51
                elif self.box4==51:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=314,y=576)
                    self.prevn4=51
                    self.pos4=52
                elif self.box4==52:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=314,y=534)
                    self.prevn4=52
                    self.pos4=53
                elif self.box4==53:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=314,y=492)
                    self.prevn4=53
                    self.pos4=54
                elif self.box4==54:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=314,y=449)
                    self.prevn4=54
                    self.pos4=55
                elif self.box4==55:
                    self.y4.destroy()
                    self.y4=Button(self.f,height=1,width=2,text="X",bg="light goldenrod yellow",command=lambda:[self.abx1(4),self.moveyel()])
                    self.y4.place(x=314,y=406)
                    self.prevn4=55
                    self.pos4=56
                elif self.box4==56:
                    self.y4.destroy()
                    self.hy4=Button(self.f,height=1,width=1,text="X",bg="light goldenrod yellow")
                    self.hy4.place(x=341,y=362)
                    self.yw+=1
            
            self.kill()
        self.tt+=1
       

       
    def movered(self):
        self.ttr=0
        self.rett()
        self.win()
        
        if self.count>=1 and self.yto==5 and self.tt<1:    #opening tokken 1
            
            self.lastmove=5
            if self.n==6 and self.siyc==0 and self.fc5==0:
                self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                self.r1.place(x=364,y=52)
                self.siyc+=1
                self.pos5=27
                
            elif self.n==1 and self.fc5==0 and self.yto==5:
                self.r1.place(x=364,y=95)
                self.prevn5=1
                self.fc5+=1
                self.pos5=28
            elif self.n==2 and self.fc5==0 and self.yto==5:
                self.r1.place(x=364,y=137)
                self.prevn5=2
                self.fc5+=1
                self.pos5=29
    
            elif self.n==3 and self.fc5==0 and self.yto==5:
                self.r1.place(x=364,y=179)
                self.prevn5=3
                self.fc5+=1
                self.pos5=30
                
            elif self.n==4 and self.fc5==0 and self.yto==5:
                self.r1.place(x=364,y=221)
                self.prevn5=4
                self.fc5+=1
                self.pos5=31
                
            elif self.n==5 and self.fc5==0 and self.yto==5:
                self.r1.place(x=407,y=262)
                self.prevn5=5
                self.fc5+=1
                self.pos5=32
                
            elif self.n==6 and self.fc5==0 and self.siyc==1 and self.yto==5:
                self.fc5+=1
                self.fsy+=1
                self.siyc+=1
                self.r1.place(x=449,y=262)
                self.prevn5=6
                self.pos5=33

            elif self.fc5>=1 and self.yto==5:                  #moving of tokken 1
                self.box5=self.prevn5+self.n
                if self.box5==2:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=137)
                    self.prevn5=2
                    self.pos5=29
                elif self.box5==3:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=179)
                    self.prevn5=3
                    self.pos5=30
                elif self.box5==4:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=221)
                    self.prevn5=4
                    self.pos5=31
                elif self.box5==5:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=407,y=262)
                    self.prevn5=5
                    self.pos5=32
                elif self.box5==6:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=449,y=262)
                    self.prevn5=6
                    self.pos5=33
                elif self.box5==7:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=491,y=262)
                    self.prevn5=7
                    self.pos5=34
                elif self.box5==8:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=533,y=262)
                    self.prevn5=8
                    self.pos5=35
                elif self.box5==9:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=575,y=262)
                    self.prevn5=9
                    self.pos5=36
                elif self.box5==10:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=617,y=262)
                    self.prevn5=10
                    self.pos5=37
                elif self.box5==11:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=617,y=304)
                    self.prevn5=11
                    self.pos5=38
                elif self.box5==12:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=617,y=362)
                    self.prevn5=12
                    self.pos5=39
                elif self.box5==13:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=575,y=362)
                    self.prevn5=13
                    self.pos5=40
                elif self.box5==14:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=533,y=362)
                    self.prevn5=14
                    self.pos5=41
                elif self.box5==15:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=491,y=362)
                    self.prevn5=15
                    self.pos5=42
                elif self.box5==16:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=449,y=362)
                    self.prevn5=16
                    self.pos5=43
                elif self.box5==17:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=407,y=362)
                    self.prevn5=17
                    self.pos5=44
                elif self.box5==18:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=406)
                    self.prevn5=18
                    self.pos5=45
                elif self.box5==19:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=449)
                    self.prevn5=19
                    self.pos5=46
                elif self.box5==20:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=492)
                    self.prevn5=20
                    self.pos5=47
                elif self.box5==21:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=534)
                    self.prevn5=21
                    self.pos5=48
                elif self.box5==22:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=576)
                    self.prevn5=22
                    self.pos5=49
                elif self.box5==23:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=364,y=618)
                    self.prevn5=23
                    self.pos5=50
                elif self.box5==24:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=304,y=618)
                    self.prevn5=24
                    self.pos5=51
                elif self.box5==25:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=618)
                    self.prevn5=25
                    self.pos5=52
                elif self.box5==26:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=575)
                    self.prevn5=26
                    self.pos5=1
                elif self.box5==27:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=534)
                    self.prevn5=27
                    self.pos5=2
                elif self.box5==28:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=492)
                    self.prevn5=28
                    self.pos5=3
                elif self.box5==29:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=449)
                    self.prevn5=29
                    self.pos5=4
                elif self.box5==30:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=406)
                    self.prevn5=30
                    self.pos5=5
                elif self.box5==31:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=218,y=362)
                    self.prevn5=31
                    self.pos5=6
                elif self.box5==32:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=178,y=362)
                    self.prevn5=32
                    self.pos5=7
                elif self.box5==33:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=138,y=362)
                    self.prevn5=33
                    self.pos5=8
                elif self.box5==34:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=98,y=362)
                    self.prevn5=34
                    self.pos5=9
                elif self.box5==35:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=52,y=362)
                    self.prevn5=35
                    self.pos5=10
                elif self.box5==36:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=10,y=362)
                    self.prevn5=36
                    self.pos5=11
                elif self.box5==37:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=10,y=304)
                    self.prevn5=37
                    self.pos5=12
                elif self.box5==38:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=10,y=262)
                    self.prevn5=38
                    self.pos5=13
                elif self.box5==39:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=50,y=262)
                    self.prevn5=39
                    self.pos5=14
                elif self.box5==40:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=98,y=262)
                    self.prevn5=40
                    self.pos5=15
                elif self.box5==41:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=138,y=262)
                    self.prevn5=41
                    self.pos5=16
                elif self.box5==42:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=178,y=262)
                    self.prevn5=42
                    self.pos5=17
                elif self.box5==43:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=218,y=262)
                    self.prevn5=43
                    self.pos5=18
                elif self.box5==44:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=221)
                    self.prevn5=44
                    self.pos5=19
                elif self.box5==45:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=179)
                    self.prevn5=45
                    self.pos5=20
                elif self.box5==46:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=137)
                    self.prevn5=46
                    self.pos5=21
                elif self.box5==47:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=95)
                    self.prevn5=47
                    self.pos5=22
                elif self.box5==48:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=52)
                    self.prevn5=48
                    self.pos5=23
                elif self.box5==49:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=262,y=10)
                    self.prevn5=49
                    self.pos5=24
                elif self.box5==50:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=314,y=10)
                    self.prevn5=50
                    self.pos5=25
                elif self.box5==51:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=314,y=52)
                    self.prevn5=51
                    self.pos5=57
                elif self.box5==52:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=314,y=95)
                    self.prevn5=52
                    self.pos5=58
                elif self.box5==53:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=314,y=137)
                    self.prevn5=53
                    self.pos5=59
                elif self.box5==54:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=314,y=179)
                    self.prevn5=54
                    self.pos5=60
                elif self.box5==55:
                    self.r1.destroy()
                    self.r1=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(5),self.movered()])
                    self.r1.place(x=314,y=221)
                    self.prevn5=55
                    self.pos5=61
                elif self.box5==56:
                    self.r1.destroy()
                    self.hr1=Button(self.f,height=1,width=1,text="X",bg="salmon1")
                    self.hr1.place(x=287,y=262)
                    self.rw+=1
            self.kill()

        if self.count>=1 and self.yto==6 and self.tt<1:    #opening tokken 2
            
            self.lastmove=6
            if self.n==6 and self.siyc2==0 and self.fc6==0:
                self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                self.r2.place(x=364,y=52)
                self.siyc2+=1
                self.pos6=27
                
            elif self.n==1 and self.fc6==0 and self.yto==6:
                self.r2.place(x=364,y=95)
                self.prevn6=1
                self.fc6+=1
                self.pos6=28
            elif self.n==2 and self.fc6==0 and self.yto==6:
                self.r2.place(x=364,y=137)
                self.prevn6=2
                self.fc6+=1
                self.pos6=29
    
            elif self.n==3 and self.fc6==0 and self.yto==6:
                self.r2.place(x=364,y=179)
                self.prevn6=3
                self.fc6+=1
                self.pos6=30
                
            elif self.n==4 and self.fc6==0 and self.yto==6:
                self.r2.place(x=364,y=221)
                self.prevn6=4
                self.fc6+=1
                self.pos6=31
                
            elif self.n==5 and self.fc6==0 and self.yto==6:
                self.r2.place(x=407,y=262)
                self.prevn6=5
                self.fc6+=1
                self.pos6=32
                
            elif self.n==6 and self.fc6==0 and self.siyc2==1 and self.yto==6:
                self.fc6+=1
                self.fsy2+=1
                self.siyc2+=1
                self.r2.place(x=449,y=262)
                self.prevn6=6
                self.pos6=33

            elif self.fc6>=1 and self.yto==6:                  #moving of tokken 2
                self.box6=self.prevn6+self.n
                if self.box6==2:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=137)
                    self.prevn6=2
                    self.pos6=29
                elif self.box6==3:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=179)
                    self.prevn6=3
                    self.pos6=30
                elif self.box6==4:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=221)
                    self.prevn6=4
                    self.pos6=31
                elif self.box6==5:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=407,y=262)
                    self.prevn6=5
                    self.pos6=32
                elif self.box6==6:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=449,y=262)
                    self.prevn6=6
                    self.pos6=33
                elif self.box6==7:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=491,y=262)
                    self.prevn6=7
                    self.pos6=34
                elif self.box6==8:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=533,y=262)
                    self.prevn6=8
                    self.pos6=35
                elif self.box6==9:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=575,y=262)
                    self.prevn6=9
                    self.pos6=36
                elif self.box6==10:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=617,y=262)
                    self.prevn6=10
                    self.pos6=37
                elif self.box6==11:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=617,y=304)
                    self.prevn6=11
                    self.pos6=38
                elif self.box6==12:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=617,y=362)
                    self.prevn6=12
                    self.pos6=39
                elif self.box6==13:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=575,y=362)
                    self.prevn6=13
                    self.pos6=40
                elif self.box6==14:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=533,y=362)
                    self.prevn6=14
                    self.pos6=41
                elif self.box6==15:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=491,y=362)
                    self.prevn6=15
                    self.pos6=42
                elif self.box6==16:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=449,y=362)
                    self.prevn6=16
                    self.pos6=43
                elif self.box6==17:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=407,y=362)
                    self.prevn6=17
                    self.pos6=44
                elif self.box6==18:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=406)
                    self.prevn6=18
                    self.pos6=45
                elif self.box6==19:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=449)
                    self.prevn6=19
                    self.pos6=46
                elif self.box6==20:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=492)
                    self.prevn6=20
                    self.pos6=47
                elif self.box6==21:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=534)
                    self.prevn6=21
                    self.pos6=48
                elif self.box6==22:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=576)
                    self.prevn6=22
                    self.pos6=49
                elif self.box6==23:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=364,y=618)
                    self.prevn6=23
                    self.pos6=50
                elif self.box6==24:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=304,y=618)
                    self.prevn6=24
                    self.pos6=51
                elif self.box6==25:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=618)
                    self.prevn6=25
                    self.pos6=52
                elif self.box6==26:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=575)
                    self.prevn6=26
                    self.pos6=1
                elif self.box6==27:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=534)
                    self.prevn6=27
                    self.pos6=2
                elif self.box6==28:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=492)
                    self.prevn6=28
                    self.pos6=3
                elif self.box6==29:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=449)
                    self.prevn6=29
                    self.pos6=4
                elif self.box6==30:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=406)
                    self.prevn6=30
                    self.pos6=5
                elif self.box6==31:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=218,y=362)
                    self.prevn6=31
                    self.pos6=6
                elif self.box6==32:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=178,y=362)
                    self.prevn6=32
                    self.pos6=7
                elif self.box6==33:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=138,y=362)
                    self.prevn6=33
                    self.pos6=8
                elif self.box6==34:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=98,y=362)
                    self.prevn6=34
                    self.pos6=9
                elif self.box6==35:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=52,y=362)
                    self.prevn6=35
                    self.pos6=10
                elif self.box6==36:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=10,y=362)
                    self.prevn6=36
                    self.pos6=11
                elif self.box6==37:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=10,y=304)
                    self.prevn6=37
                    self.pos6=12
                elif self.box6==38:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=10,y=262)
                    self.prevn6=38
                    self.pos6=13
                elif self.box6==39:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=50,y=262)
                    self.prevn6=39
                    self.pos6=14
                elif self.box6==40:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=98,y=262)
                    self.prevn6=40
                    self.pos6=15
                elif self.box6==41:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=138,y=262)
                    self.prevn6=41
                    self.pos6=16
                elif self.box6==42:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=178,y=262)
                    self.prevn6=42
                    self.pos6=17
                elif self.box6==43:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=218,y=262)
                    self.prevn6=43
                    self.pos6=18
                elif self.box6==44:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=221)
                    self.prevn6=44
                    self.pos6=19
                elif self.box6==45:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=179)
                    self.prevn6=45
                    self.pos6=20
                elif self.box6==46:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=137)
                    self.prevn6=46
                    self.pos6=21
                elif self.box6==47:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=95)
                    self.prevn6=47
                    self.pos6=22
                elif self.box6==48:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=52)
                    self.prevn6=48
                    self.pos6=23
                elif self.box6==49:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=262,y=10)
                    self.prevn6=49
                    self.pos6=24
                elif self.box6==50:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=314,y=10)
                    self.prevn6=50
                    self.pos6=25
                elif self.box6==51:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=314,y=52)
                    self.prevn6=51
                    self.pos6=57
                elif self.box6==52:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=314,y=95)
                    self.prevn6=52
                    self.pos6=58
                elif self.box6==53:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=314,y=137)
                    self.prevn6=53
                    self.pos6=59
                elif self.box6==54:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=314,y=179)
                    self.prevn6=54
                    self.pos6=60
                elif self.box6==55:
                    self.r2.destroy()
                    self.r2=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(6),self.movered()])
                    self.r2.place(x=314,y=221)
                    self.prevn6=55
                    self.pos6=61
                elif self.box6==56:
                    self.r2.destroy()
                    self.hr2=Button(self.f,height=1,width=1,text="X",bg="salmon1")
                    self.hr2.place(x=305,y=262)
                    self.rw+=1
            
            self.kill()


        if self.count>=1 and self.yto==7 and  self.tt<1:    #opening tokken 3
            
            self.lastmove=7
            if self.n==6 and self.siyc3==0 and self.fc7==0:
                self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                self.r3.place(x=364,y=52)
                self.siyc3+=1
                self.pos7=27
               
                
            elif self.n==1 and self.fc7==0 and self.yto==7:
                self.r3.place(x=364,y=95)
                self.prevn7=1
                self.fc7+=1
                self.pos7=28
            elif self.n==2 and self.fc7==0 and self.yto==7:
                self.r3.place(x=364,y=137)
                self.prevn7=2
                self.fc7+=1
                self.pos7=29
    
            elif self.n==3 and self.fc7==0 and self.yto==7:
                self.r3.place(x=364,y=179)
                self.prevn7=3
                self.fc7+=1
                self.pos7=30
                
            elif self.n==4 and self.fc7==0 and self.yto==7:
                self.r3.place(x=364,y=221)
                self.prevn7=4
                self.fc7+=1
                self.pos7=31
                
            elif self.n==5 and self.fc7==0 and self.yto==7:
                self.r3.place(x=407,y=262)
                self.prevn7=5
                self.fc7+=1
                self.pos7=32
                
            elif self.n==6 and self.fc7==0 and self.siyc3==1 and self.yto==7:
                self.fc7+=1
                self.fsy3+=1
                self.siyc3+=1
                self.r3.place(x=449,y=262)
                self.prevn7=6
                self.pos7=33

            elif self.fc7>=1 and self.yto==7:                  #moving of tokken 3
                self.box7=self.prevn7+self.n
                if self.box7==2:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=137)
                    self.prevn7=2
                    self.pos7=29
                elif self.box7==3:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=179)
                    self.prevn7=3
                    self.pos7=30
                elif self.box7==4:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=221)
                    self.prevn7=31
                elif self.box7==5:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=407,y=262)
                    self.prevn7=5
                    self.pos7=31
                elif self.box7==6:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=449,y=262)
                    self.prevn7=6
                    self.pos7=33
                elif self.box7==7:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=491,y=262)
                    self.prevn7=7
                    self.pos7=34
                elif self.box7==8:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=533,y=262)
                    self.prevn7=8
                    self.pos7=35
                elif self.box7==9:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=575,y=262)
                    self.prevn7=9
                    self.pos7=36
                elif self.box7==10:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=617,y=262)
                    self.prevn7=10
                    self.pos7=37
                elif self.box7==11:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=617,y=304)
                    self.prevn7=11
                    self.pos7=38
                elif self.box7==12:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=617,y=362)
                    self.prevn7=12
                    self.pos7=39
                elif self.box7==13:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=575,y=362)
                    self.prevn7=13
                    self.pos7=40
                elif self.box7==14:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=533,y=362)
                    self.prevn7=14
                    self.pos7=41
                elif self.box7==15:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=491,y=362)
                    self.prevn7=15
                    self.pos7=42
                elif self.box7==16:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=449,y=362)
                    self.prevn7=16
                    self.pos7=43
                elif self.box7==17:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=407,y=362)
                    self.prevn7=17
                    self.pos7=44
                elif self.box7==18:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=406)
                    self.prevn7=18
                    self.pos7=45
                elif self.box7==19:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=449)
                    self.prevn7=19
                    self.pos7=46
                elif self.box7==20:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=492)
                    self.prevn7=20
                    self.pos7=47
                elif self.box7==21:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=534)
                    self.prevn7=21
                    self.pos7=48
                elif self.box7==22:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=576)
                    self.prevn7=22
                    self.pos7=49
                elif self.box7==23:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=364,y=618)
                    self.prevn7=23
                    self.pos7=50
                elif self.box7==24:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=304,y=618)
                    self.prevn7=24
                    self.pos7=51
                elif self.box7==25:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=618)
                    self.prevn7=25
                    self.pos7=52
                elif self.box7==26:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=575)
                    self.prevn7=26
                    self.pos7=1
                elif self.box7==27:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=534)
                    self.prevn7=27
                    self.pos7=2
                elif self.box7==28:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=492)
                    self.prevn7=28
                    self.pos7=3
                elif self.box7==29:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=449)
                    self.prevn7=29
                    self.pos7=4
                elif self.box7==30:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=406)
                    self.prevn7=30
                    self.pos7=5
                elif self.box7==31:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=218,y=362)
                    self.prevn7=31
                    self.pos7=6
                elif self.box7==32:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=178,y=362)
                    self.prevn7=32
                    self.pos7=7
                elif self.box7==33:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=138,y=362)
                    self.prevn7=33
                    self.pos7=8
                elif self.box7==34:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=98,y=362)
                    self.prevn7=34
                    self.pos7=9
                elif self.box7==35:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=52,y=362)
                    self.prevn7=35
                    self.pos7=10
                elif self.box7==36:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=10,y=362)
                    self.prevn7=36
                    self.pos7=11
                elif self.box7==37:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=10,y=304)
                    self.prevn7=37
                    self.pos7=12
                elif self.box7==38:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=10,y=262)
                    self.prevn7=38
                    self.pos7=13
                elif self.box7==39:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=50,y=262)
                    self.prevn7=39
                    self.pos7=14
                elif self.box7==40:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=98,y=262)
                    self.prevn7=40
                    self.pos7=15
                elif self.box7==41:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=138,y=262)
                    self.prevn7=41
                    self.pos7=16
                elif self.box7==42:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=178,y=262)
                    self.prevn7=42
                    self.pos7=17
                elif self.box7==43:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=218,y=262)
                    self.prevn7=43
                    self.pos7=18
                elif self.box7==44:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=221)
                    self.prevn7=44
                    self.pos7=19
                elif self.box7==45:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=179)
                    self.prevn7=45
                    self.pos7=20
                elif self.box7==46:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=137)
                    self.prevn7=46
                    self.pos7=21
                elif self.box7==47:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=95)
                    self.prevn7=47
                    self.pos7=22
                elif self.box7==48:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=52)
                    self.prevn7=48
                    self.pos7=23
                elif self.box7==49:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=262,y=10)
                    self.prevn7=49
                    self.pos7=24
                elif self.box7==50:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=314,y=10)
                    self.prevn7=50
                    self.pos7=25
                elif self.box7==51:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=314,y=52)
                    self.prevn7=51
                    self.pos7=57
                elif self.box7==52:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=314,y=95)
                    self.prevn7=52
                    self.pos7=58
                elif self.box7==53:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=314,y=137)
                    self.prevn7=53
                    self.pos7=59
                elif self.box7==54:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=314,y=179)
                    self.prevn7=54
                    self.pos7=60
                elif self.box7==55:
                    self.r3.destroy()
                    self.r3=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(7),self.movered()])
                    self.r3.place(x=314,y=221)
                    self.prevn7=55
                    self.pos7=61
                elif self.box7==56:
                    self.r3.destroy()
                    self.hr3=Button(self.f,height=1,width=1,text="X",bg="salmon1")
                    self.hr3.place(x=323,y=262)
                    self.rw+=1
            
            self.kill()

        if self.count>=1 and self.yto==8 and  self.tt<1:    #opening tokken 4
            
            self.lastmove=8
            if self.n==6 and self.siyc4==0 and self.fc8==0:
                self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                self.r4.place(x=364,y=52)
                self.siyc4+=1
                self.pos8=27
                
            elif self.n==1 and self.fc8==0 and self.yto==8:
                self.r4.place(x=364,y=95)
                self.prevn8=1
                self.fc8+=1
                self.pos8=28
            elif self.n==2 and self.fc8==0 and self.yto==8:
                self.r4.place(x=364,y=137)
                self.prevn8=2
                self.fc8+=1
                self.pos8=29
    
            elif self.n==3 and self.fc8==0 and self.yto==8:
                self.r4.place(x=364,y=179)
                self.prevn8=3
                self.fc8+=1
                self.pos8=30
                
            elif self.n==4 and self.fc8==0 and self.yto==8:
                self.r4.place(x=364,y=221)
                self.prevn8=4
                self.fc8+=1
                self.pos8=31
                
            elif self.n==5 and self.fc8==0 and self.yto==8:
                self.r4.place(x=407,y=262)
                self.prevn8=5
                self.fc8+=1
                self.pos8=32
                
            elif self.n==6 and self.fc8==0 and self.siyc4==1 and self.yto==8:
                self.fc8+=1
                self.fsy4+=1
                self.siyc4+=1
                self.r4.place(x=449,y=262)
                self.prevn8=6
                self.pos8=33

            elif self.fc8>=1 and self.yto==8:                  #moving of tokken 4
                self.box8=self.prevn8+self.n
                if self.box8==2:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=137)
                    self.prevn8=2
                    self.pos8=29
                elif self.box8==3:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=179)
                    self.prevn8=3
                    self.pos8=30
                elif self.box8==4:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=221)
                    self.prevn8=4
                    self.pos8=31
                elif self.box8==5:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=407,y=262)
                    self.prevn8=5
                    self.pos8=32
                elif self.box8==6:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=449,y=262)
                    self.prevn8=6
                    self.pos8=33
                elif self.box8==7:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=491,y=262)
                    self.prevn8=7
                    self.pos8=34
                elif self.box8==8:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=533,y=262)
                    self.prevn8=8
                    self.pos8=35
                elif self.box8==9:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=575,y=262)
                    self.prevn8=9
                    self.pos8=36
                elif self.box8==10:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=617,y=262)
                    self.prevn8=10
                    self.pos8=37
                elif self.box8==11:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=617,y=304)
                    self.prevn8=11
                    self.pos8=38
                elif self.box8==12:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=617,y=362)
                    self.prevn8=12
                    self.pos8=39
                elif self.box8==13:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=575,y=362)
                    self.prevn8=13
                    self.pos8=40
                elif self.box8==14:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=533,y=362)
                    self.prevn8=14
                    self.pos8=41
                elif self.box8==15:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=491,y=362)
                    self.prevn8=15
                    self.pos8=42
                elif self.box8==16:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=449,y=362)
                    self.prevn8=16
                    self.pos8=43
                elif self.box8==17:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=407,y=362)
                    self.prevn8=17
                    self.pos8=44
                elif self.box8==18:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=406)
                    self.prevn8=18
                    self.pos8=45
                elif self.box8==19:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=449)
                    self.prevn8=19
                    self.pos8=46
                elif self.box8==20:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=492)
                    self.prevn8=20
                    self.pos8=47
                elif self.box8==21:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=534)
                    self.prevn8=21
                    self.pos8=48
                elif self.box8==22:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=576)
                    self.prevn8=22
                    self.pos8=49
                elif self.box8==23:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=364,y=618)
                    self.prevn8=23
                    self.pos8=50
                elif self.box8==24:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=304,y=618)
                    self.prevn8=24
                    self.pos8=51
                elif self.box8==25:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=618)
                    self.prevn8=25
                    self.pos8=52
                elif self.box8==26:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=575)
                    self.prevn8=26
                    self.pos8=1
                elif self.box8==27:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=534)
                    self.prevn8=27
                    self.pos8=2
                elif self.box8==28:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=492)
                    self.prevn8=28
                    self.pos8=3
                elif self.box8==29:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=449)
                    self.prevn8=29
                    self.pos8=4
                elif self.box8==30:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=406)
                    self.prevn8=30
                    self.pos8=5
                elif self.box8==31:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=218,y=362)
                    self.prevn8=31
                    self.pos8=6
                elif self.box8==32:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=178,y=362)
                    self.prevn8=32
                    self.pos8=7
                elif self.box8==33:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=138,y=362)
                    self.prevn8=33
                    self.pos8=8
                elif self.box8==34:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=98,y=362)
                    self.prevn8=34
                    self.pos8=9
                elif self.box8==35:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=52,y=362)
                    self.prevn8=35
                    self.pos8=10
                elif self.box8==36:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=10,y=362)
                    self.prevn8=36
                    self.pos8=11
                elif self.box8==37:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=10,y=304)
                    self.prevn8=37
                    self.pos8=12
                elif self.box8==38:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=10,y=262)
                    self.prevn8=38
                    self.pos8=13
                elif self.box8==39:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=50,y=262)
                    self.prevn8=39
                    self.pos8=14
                elif self.box8==40:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=98,y=262)
                    self.prevn8=40
                    self.pos8=15
                elif self.box8==41:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=138,y=262)
                    self.prevn8=41
                    self.pos8=16
                elif self.box8==42:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=178,y=262)
                    self.prevn8=42
                    self.pos8=17
                elif self.box8==43:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=218,y=262)
                    self.prevn8=43
                    self.pos8=18
                elif self.box8==44:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=221)
                    self.prevn8=44
                    self.pos8=19
                elif self.box8==45:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=179)
                    self.prevn8=45
                    self.pos8=20
                elif self.box8==46:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=137)
                    self.prevn8=46
                    self.pos8=21
                elif self.box8==47:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=95)
                    self.prevn8=47
                    self.pos8=22
                elif self.box8==48:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=52)
                    self.prevn8=48
                    self.pos8=23
                elif self.box8==49:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=262,y=10)
                    self.prevn8=49
                    self.pos8=24
                elif self.box8==50:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=314,y=10)
                    self.prevn8=50
                    self.pos8=25
                elif self.box8==51:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=314,y=52)
                    self.prevn8=51
                    self.pos8=57
                elif self.box8==52:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=314,y=95)
                    self.prevn8=52
                    self.pos8=58
                elif self.box8==53:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=314,y=137)
                    self.prevn8=53
                    self.pos8=59
                elif self.box8==54:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=314,y=179)
                    self.prevn8=54
                    self.pos8=60
                elif self.box8==55:
                    self.r4.destroy()
                    self.r4=Button(self.f,height=1,width=2,text="X",bg="salmon1",command=lambda:[self.abx1(8),self.movered()])
                    self.r4.place(x=314,y=221)
                    self.prevn8=55
                    self.pos8=61
                elif self.box8==56:
                    self.r4.destroy()
                    self.hr4=Button(self.f,height=1,width=1,text="X",bg="salmon1")
                    self.hr4.place(x=341,y=262)
                    self.rw+=1
            
            self.kill()
        self.tt+=1
    
        





 
r=Tk()
r.title("LUDO")
h=home(r)
r.title("LUDO KNIGHT CAPTCHA VERIFY")
r.mainloop()


