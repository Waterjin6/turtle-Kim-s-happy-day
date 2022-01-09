from tkinter import *
import turtle
import random

##공격물의 개수를 여기서 정한다.
SIZE = 20

##필요한 배열들
objects=[]
objcol=["gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "darkgreen", "chocolate", "brown", "black","gray"]
objsha=["square","circle","triangle"]
osay = ["잘지내지?", "안녕?", "어이쿠 미안해요!","반가워:)", "깜짝이야!"]
psay = ["공격? 난 폭력은 싫어해", "폭행죄 최대 벌금 천만원!", "김거북은 평화주의자라네","무조건 폭력으로 해결하려는 태도는 좋지않아.", "나들이 중에 타인을 공격할 이유는?",
        "..공격??? 농담이지?;", "친구들한테 총쏘고 그러면 안되는 거야.","내 이웃을 사랑하라"]

def howto(): ##게임방법을 선택하면 실행된다.
    win = Tk()
    win.title("안녕안녕")
    win.geometry("300x170")
    l0 = Label(win, text = "")
    l1 = Label(win, text = "< 방향키로 조준하고 Z키로 발사하라! >",font = "helvetica 12 bold")
    l2 = Label(win, text = "")
    l3 = Label(win, text = "<- 방향키 : 왼쪽으로 김거북을 회전한다.")
    l4 = Label(win, text = "-> 방향키 : 오른쪽으로 김거북을 회전한다.")
    l5 = Label(win, text = "스페이스 바 : 김거북을 전진시킨다")
    l6 = Label(win, text = "Z키 : 총알을 발사한다")
    l0.pack()
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l6.pack()
   
def bhappy(): ##행복해질래를 선택하면 실행된다.
    win = Tk()
    win.title("행복이라..")
    win.geometry("250x50")
    l1 = Label(win, text = "행복은 스스로 찾는거야 : )", font = "helvetica 12 bold")
    l2 = Label(win, text = "    -김거북")
    l1.pack()
    l2.pack()
    
def bye(): ##종료를 선택하면 실행된다.
    win.destroy()
    turtle.bye()
    bi = Tk()
    bi.title("놀아줘서 고마워!")
    bi.geometry("300x50")
    l1 = Label(bi, text = "즐거운 나들이였어.", font = "helvetica 12 bold")
    l2 = Label(bi, text = "    -김거북 : )")
    l1.pack()
    l2.pack()
    bi.mainloop()
    
def startgame():##시작을 선택하면 실행된다.
    
    def turnleft():
        player.left(30)
    def turnright():
        player.right(30)
    def gogo():
        player.forward(2)
    def fire():#z키를 눌면 실행된다.
        player.write(psay[random.randint(0,7)])
        
    def play():#게임 진행을 위해 필요하다(10ms마다 실행된다)
        for o in objects:
            o.forward(2)

            if player.distance(o)<12:
                o.write(osay[random.randint(0,4)])
            if player.distance(o)>600:
                o.goto(random.randint(-300,300),random.randint(-300,300))
        screen.ontimer(play,10)

    # 게임화면의 상단 글자 쓰기    
    word = turtle.Turtle()
    word.hideturtle()
    
    word.penup()
    word.setpos(-370,290)
    word.pendown()
    word.write("Z 키 : 공격(총알발사)", font = "helvetica 14 bold")

    word.penup()
    word.setpos(160,290)
    word.pendown()   
    word.write("[ 점수 : 즐거우면 됐어 ! ]", font = "helvetica 14 bold")

    # 김거북 만들기
    player = turtle.Turtle()
    player.color("Green")
    player.shape("turtle")
    player.penup()
    player.speed(0)
    screen = player.getscreen()
    screen.onkeypress(turnleft, "Left")
    screen.onkeypress(turnright, "Right")
    screen.onkeypress(gogo, "space")
    screen.onkeypress(fire, "z")
    screen.listen()

    #공격물 만들기
    for i in range(0, SIZE):
        a1 = turtle.Turtle()
        a1.color(objcol[i%18])
        a1.shape(objsha[i%3])
        a1.penup()
        a1.speed(0)
        a1.goto(random.randint(-300,300),random.randint(-300,300))
        a1.left(random.randint(-180,180))
        objects.append(a1)
    
    screen.ontimer(play, 10)#게임 실행
    
##시작 창 만들기   
win = Tk()
win.title("......슈팅게임...사실 누군가를 공격하는 건 싫어")
win.geometry('250x220')

#시작 화면 디자인
ml1 = Label(win, text = "김거북의",font =' helvetica 25 bold',relief = "solid",background='yellow')
ml2 = Label(win, text = "멋진 나들이 : )",font =' helvetica 25 bold')
start = Button(win, text = "시작", fg = "white", font = 'helvetica 10 bold', bg = "red",command = startgame)
how = Button(win, text = "게임방법", fg = "white", font = 'helvetica 10 bold',bg = "green", command = howto)
end = Button(win, text = "종료", fg = "white", font = 'helvetica 10 bold', bg = "blue", command = bye)
happy = Button(win, text = "행복해질래",bg = "pink", command =bhappy)

ml1.place( x= 20, y =30)
ml2.place( x= 20, y =100)
start.place(x=20, y=170)
how.place(x= 90, y = 170)
end.place(x= 190, y =170)
happy.place(x = 30, y = 250, width =180, height=30)

win.mainloop()
