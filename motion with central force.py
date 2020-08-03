'''This program calculate the location of planet near a star like the sun according to newton's second law and gravitational force.
You can play with vx and vy as the start velocity in each direction.
In low velocities , the planet may fall into the sun.
In moderate velocity the planet have elliptic path.
In high velocity , the planet escapes the sun.'''

from graphics import *
import time
import math
def distance(x1,y1,x2,y2):
    d1 = x2-x1
    d2 = y2-y1
    dis2 = math.pow(d1, 2)+math.pow(d2, 2)
    d = math.sqrt(dis2)
    return d

def main():
    x =300
    y = 650.0
    xc = 500.0
    yc = 500.0
    vx = 0.5
    vy = 0.3
    t = 0.0001 #hour
    win = GraphWin("My window", 1000, 1000)
    win.setBackground('black')
    pt0 = Point(xc, yc)
    cir0 = Circle(pt0, 10)
    cir0.setFill('yellow')
    cir0.draw(win)
    d = distance(x, y, xc, yc)
    f = 237.155 / (math.pow(d, 2))
    fx0 = (abs(x - xc) / d) * f  # (x-xc)/d for cos
    fy0 = (abs(y - yc) / d) * f  # (y-yc/d for sin

    x = x + vx * t + fx0 * math.pow(t, 2) / 2.
    y = y + vy * t + fy0 * math.pow(t, 2) / 2.
    vx = vx + fx0 * t
    vy = vy + fy0 * t


    for index in range(50000000):
        d = distance(x, y, xc, yc)
        if d<= 10:
            cir = Circle(pt, 10)
            break
        f = 237.155/(math.pow(d, 2))
        fx = (abs(x-xc)/ d) * f    #(x-xc)/d for cos
        fy = (abs(y-yc) / d) * f    # (y-yc/d for sin
        if y > yc and x>xc:
            fy = -abs(fy)
            fx= -abs(fx)
        if x>xc and y<yc:
            fx = -abs(fx)
            fy= abs(fy)
        if y < yc and x<xc:
            fy=abs(fy)
            fx=abs(fx)
        if x<xc and y>yc:
            fx=abs(fx)
            fy=-abs(fy)
        fx_av=(fx+fx0)/2.
        fy_av=(fy+fy0)/2.
        fx0=fx
        fy0=fy
        x = x + vx*t + fx_av*math.pow(t, 2)/2.
        y = y + vy * t + fy_av * math.pow(t, 2) / 2.
        vx = vx +fx_av * t
        vy = vy + fy_av *t
        if index%10000==0:      #to draw only part of the calculations

            pt = Point(x, y)
            cir = Circle(pt, 5)
            cir2 = Circle(pt, 5)
            cir2.setFill('gray')
            cir2.setOutline('white')
            cir2.draw(win)
            time.sleep(0.01)

    win.getMouse()
    win.close()
main()