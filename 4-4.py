import math
def circle(t , r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t , n , length)