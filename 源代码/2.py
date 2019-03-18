#e2.利用turtle绘制S图形
import turtle
def DrawS():
    turtle.seth(100)
    turtle.circle(40,250)
    turtle.seth(-20)
    turtle.fd(20)
    turtle.circle(-40,250)
    turtle.hideturtle()    
def main():
    turtle.setup(700,500,200,200)
    turtle.pensize(10)
    turtle.pencolor('red')
    DrawS()          
main()
