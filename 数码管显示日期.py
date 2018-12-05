import turtle
import time
def drawgap():
    turtle.penup()
    turtle.fd(4)
def drawline(draw):
    drawgap()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)
def drawdight(dight):
    if dight in [2,3,4,5,6,8,9]:  
        drawline(True) 
    else:
        drawline(False)
    if dight in [0,1,3,4,5,6,7,8,9]: 
        drawline(True)
    else:
        drawline(False)
    if dight in [0,2,3,5,6,8,9]:
        drawline(True)
    else:
        drawline(False)
    if dight in [0,2,6,8]: 
        drawline(True)
    else:
        drawline(False)
    turtle.left(90)
    if dight in [0,4,5,6,8,9]: 
        drawline(True)
    else:
        drawline(False)
    if dight in [0,2,3,5,6,7,8,9]: 
        drawline(True)
    else:
        drawline(False)
    if dight in [0,1,2,3,4,7,8,9]: 
        drawline(True)
    else:
        drawline(False)
    turtle.right(180)
    turtle.penup()
    turtle.fd(20)

def drawdate(date):        
    for i in date:
        if i =="-":
            turtle.pencolor("green")
            turtle.write("年",font=("Arial",18,"normal"))
            turtle.penup()
            turtle.fd(40)
        elif i =="+":
            turtle.pencolor("blue")
            turtle.write("月",font=("Arial",18,"normal"))
            turtle.penup()
            turtle.fd(40)
        elif i =="=":
            turtle.pencolor("red")
            turtle.write("日",font=("Arial",18,"normal"))
        else:
            turtle.pencolor("black")
            drawdight(eval(i))
def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.pensize(5)
    turtle.fd(-300)
    drawdate(time.strftime("%Y-%m+%d=",time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()


