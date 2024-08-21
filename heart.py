from turtle import *
import math

#calculates the y-coordinate of the point on the heart curve
def calculateY(k):
    return 13*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

#calculates the x-coordinate of the point on the heart curve
def calculateX(k):
    return 15*math.sin(k)**3

#initialized turtle
speed(0)
bgcolor("black")

for i in range(1000):
    x = calculateX(i) * 20
    y = calculateY(i) * 20

    #moves turtle to point on heart
    goto(x, y)

    #set color
    color("#FFB6C1")

    #returns to origin to color
    goto(0, 0)

done()