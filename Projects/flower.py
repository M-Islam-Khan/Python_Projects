from turtle import*
def disp():
    for i in range(300):
        color("red","yellow")
        speed(15)
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
disp()
mainloop()