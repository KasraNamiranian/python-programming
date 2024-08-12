import turtle
def polygon(t,n,length):
    deg=360/n #andaze har zavie kharejie yek chand zeli montazam
    for i in range(n):
        t.fd(length)
        t.lt(deg)

bob=turtle.Turtle()
square(bob,12,100)
turtle.mainloop()