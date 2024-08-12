import turtle
import math


def polygon(t,n,length):
    deg=360/n #andaze har zavie kharejie yek chand zeli montazam
    for i in range(n):
        t.fd(length)
        t.lt(deg)


def circle(t , r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t , n , length)

bob=turtle.Turtle()
circle(bob,50)
turtle.mainloop()