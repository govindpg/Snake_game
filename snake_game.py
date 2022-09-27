
import turtle
import time
import random


delay=0.1

wn=turtle.Screen()
wn.title("snake game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#snakehead
hd=turtle.Turtle()
hd.speed(0)
hd.shape("square")
hd.color("white")
hd.penup()
hd.goto(0,0)
hd.direction ='stop'

#food
fd=turtle.Turtle()
fd.speed(0)
fd.shape("square")
fd.color("red")
fd.penup()
fd.goto(0,100)

segments= []


#functions
def go_up():
    if hd.direction != "down":
        hd.direction="up"

def go_down():
    if hd.direction != "up":
        hd.direction="down"


def go_right():
    if hd.direction != "left":
        hd.direction="right"


def go_left():
    if hd.direction != "right":
        hd.direction="left"



def move():
    if hd.direction == "up":
        y=hd.ycor()
        hd.sety(y+20)
    
    if hd.direction == "down":
        y=hd.ycor()
        hd.sety(y-20)
    
    if hd.direction == "left":
        x=hd.xcor()
        hd.setx(x-20)
    
    if hd.direction == "right":
        x=hd.xcor()
        hd.setx(x+20)


#keyboard
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")





while True:
    wn.update()
    

    #collotion with border
    if hd.xcor()>290 or hd.xcor()<-290 or hd.ycor()>290 or hd.ycor()<-290:
        time.sleep(1)
        hd.goto(0,0)
        hd.direction = "stop"
    
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()
    

    if hd.distance(fd)<20:
        #move food to random postion
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        fd.goto(x,y)

        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1,0,-1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)

    if len(segments)> 0:
        x=hd.xcor()
        y=hd.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(hd)< 20:
            time.sleep(1)
            hd.goto(0,0)
            hd.direction = "stop"
        
            for segment in segments:
                segment.goto(1000,1000)
    
            segments.clear()


    time.sleep(delay)
    
wn.mainloop()


