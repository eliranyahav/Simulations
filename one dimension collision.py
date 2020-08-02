#Elastic collision
from graphics import *
import time
import math

def main():
    x1=100.
    x2=700.
    v1=25.
    v2=-30.
    r=50
    m1=3
    m2=0.5
    t=0.05
    win = GraphWin("My win", 800, 600)
    win.setBackground('black')
    pt0 = Point(x1,300)
    cir0 = Circle(pt0, r*m1)
    cir0.setFill('yellow')
    cir0.draw(win)
    pt1 = Point(x2, 300)
    cir1 = Circle(pt1,r*m2)
    cir1.setFill('yellow')
    cir1.draw(win)
    time.sleep(1)
    for i in range (2000):

        if abs(x2-x1)<=(r*m1+r*m2):
            u2=(2*m1*v1+m2*v2-m1*v2)/(m1+m2)
            v1=v2+u2-v1
            v2=u2
        x1 = x1 + v1 * t
        x2 = x2 + v2 * t
        pt0=Point(x1,300)
        pt1=Point(x2,300)
        cir0.undraw()
        cir1.undraw()

        cir0=Circle(pt0,r*m1)
        cir1=Circle(pt1,r*m2)
        cir0.setFill('yellow')
        cir1.setFill('yellow')

        cir0.draw(win)
        cir1.draw(win)
        time.sleep(0.05)
    win.getMouse()
    win.close()

main()