# This is a program to draw a digit.
import turtle
import time
def drawgap():
    turtle.penup()
    turtle.fd(5)
def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit):
    drawline(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 8] else drawline(False)
    drawline(True) if digit in [0, 2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0, 4, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawline(False)
    drawline(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawdate(date):
    for i in date:
        drawdigit(eval(i))

def main():
    turtle.setup(1280, 720)
    turtle.penup()
    turtle.pensize(10)
    turtle.speed(10)
    turtle.fd(-500)
    now = time.strftime("%Y%m%d%H%M%S", time.gmtime())
    drawdate(now)
    turtle.hideturtle()
    turtle.done()


main()