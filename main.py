import turtle
import time
from tkinter import *
from tkinter.messagebox import showerror, askquestion
import sys
dx=0
dy=0

master = Tk()
def enter(event):
    button.config(relief=GROOVE, fg='black', bg='grey')

def leave(event):
    button.config(relief=RAISED, fg='yellow', bg='red')

def button1():
    global dx,dy
    value = spin.get()
    if value in ['Beginner','Normal','Pro','Expert','Veteran']:

        if value=='Beginner':
            dx=0.2
            dy=-0.2
            master.destroy()

        elif value=='Normal':
            dx=-0.3
            dy=-0.3
            master.destroy()

        elif value=='Pro':
            dx=0.5
            dy=-0.5
            master.destroy()

        elif value=='Expert':
            dx=0.7
            dy=-0.7
            master.destroy()

        elif value=='Veteran':
            dx=1
            dy=-1
            master.destroy()
    else:
        showerror('M-PONG','Please select a valid difficulty level!')

def close():
    result = askquestion('M-PONG','Do you want to exit?')
    if result=='yes':
        sys.exit()
    else:
        pass

master.config(background='black')
master.resizable(0,0)
master.geometry('300x150+600+300')
master.title('M-PONG')
master.protocol('WM_DELETE_WINDOW',close)
label1 = Label(master,text='Welcome To M-PONG!',font='cursive 15 bold italic',fg='white',bg='black').pack()
label2 = Label(master,text='Select Your In-Game Difficulty: ',font='cursibe 9 bold italic',bg='black',fg='white').place(x=20,y=50)
spin = Spinbox(master,values=('Beginner','Normal','Pro','Expert','Veteran'),width=10)
spin.place(x=210,y=51)
button = Button(master,text='PLAY!',fg='yellow',bg='red',activeforeground='red',activebackground='yellow',borderwidth=4,font='cursive 12 bold italic',cursor='hand2',command=button1)
button.pack(side=BOTTOM)
button.bind('<Enter>',enter)
button.bind('<Leave>',leave)
master.mainloop()

wn = turtle.Screen()
wn.title("Pong By Muzammil")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a=0
score_b=0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: {}     Player B: {}.'.format(score_a,score_b),align='center',font=('Arial 16 bold'))
# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 50
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 50
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 50
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 50
	paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:

    wn.update()

	# Move the ball
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

	# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        dx *= -1
        score_a+=1
        pen.clear()
        pen.write('Player A: {}     Player B: {}.'.format(score_a, score_b), align='center', font=('Arial 16 bold'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        dx *= -1
        score_b+=1
        pen.clear()
        pen.write('Player A: {}     Player B: {}.'.format(score_a, score_b), align='center', font=('Arial 16 bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        dx *= -1

    if score_a==5:
        pen.clear()
        pen.write('Player A Wins',align='center',font='Arial 18 bold')
        time.sleep(1)
        break

    if score_b==5:
        pen.clear()
        pen.write('Player B Win')
        pen.write('Player B wins',align='center',font='Arial 18 bold')
        time.sleep(1)
        break
