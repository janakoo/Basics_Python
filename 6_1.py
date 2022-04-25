from time import sleep
import turtle


t = turtle.Turtle()
t.screen.setup(800, 800)
def circle(x,y,r,color):
    t.up()
    t.goto(x,y-r)
    t.down()
    t.fillcolor("white")
    if (color==1):
     t.fillcolor("red")
    if (color==2):
     t.fillcolor("yellow")
    if (color==3):
     t.fillcolor("green")
    if (color==4):
     t.fillcolor("blue")
    t.begin_fill()
    t.circle(r,360)
    t.end_fill()
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый', 'Желтый']

    def running(self):
        i = 0
        while i != 4:
            print(TrafficLight.__color[i])
            if i == 0:
                circle(20, 50, 100, 0)
                circle(20, -150, 100, 0)
                circle(20, 250, 100, 1)
                sleep(7)
            elif i == 1:
                circle(20, 250, 100, 0)
                circle(20, -150, 100, 0)
                circle(20, 50, 100, 2)
                sleep(2)
            elif i == 2:
                circle(20, 250, 100, 0)
                circle(20, 50, 100, 0)
                circle(20, -150, 100, 3)
                sleep(5)
            elif i == 3:
                circle(20, 50, 100, 0)
                circle(20, -150, 100, 0)
                circle(20, 250, 100, 1)
                sleep(2)
            i += 1


ligth = TrafficLight()
ligth.running()
t.screen.exitonclick()
t.screen.mainloop()