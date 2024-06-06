import turtle
def square(t,n):
    deg=360/n #andaze har zavie kharejie yek chand zeli montazam
    for i in range(n):
        t.fd(100)
        t.lt(deg)

bob=turtle.Turtle()
square(bob,12)
turtle.mainloop()