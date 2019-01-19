from turtle import *
from time import *


def draw(len,target):
    tasks="000"
    step,depth = len/(3**target),0
    while depth<target:
        depth+=1
        tasks = ''.join([s+str(depth)*2+s for s in tasks])
    pre=''
    for task in tasks:
        if pre==task:
            right(120)
        else:
            left(60)
        forward(step)
        pre = task


length = 300.0
speed(10)
start = perf_counter()
draw(length,3)
end = perf_counter()
penup()
goto(-200, 0)
pendown()
write(str(int(end - start)), font=("Arial", 18, "normal"))
hideturtle()
done()

