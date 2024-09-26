from gturtle import *
import datetime

makeTurtle()
hideTurtle()

def dial():
    setPenColor("black")
    setPenWidth(15)
    penUp()
    repeat 12:
        forward(210)
        penDown()
        backward(30)
        penUp()
        forward(30)
        backward(210)
        right(360/12)
    
    setPenWidth(3)
    repeat 60:
        forward(210)
        penDown()
        backward(10)
        penUp()
        forward(10)
        backward(210)
        right(360/60)
    penDown()
        
def secondsHand(second):
    heading(360/60*second)
    setPenWidth(7)
    setPenColor("red")
    forward(180)
    dot(35)
    backward(180)

def hand(length):
    setPenWidth(15)
    setPenColor("black")
    forward(length)
    backward(length)

def minutesHand(minute):
    heading(360/60*minute)
    hand(160)

def hourHand(hour):
    heading(360/12*hour)
    hand(120)

def clock():
    dial()
    savePlayground()
    repeat:
        currentTime=datetime.datetime.now()
        minutesHand(currentTime.minute)
        hourHand(currentTime.hour)
        secondsHand(currentTime.second)
        delay(20)
        clear()

clock()
