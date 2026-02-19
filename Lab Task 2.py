 # Question no.1
import turtle
  # Make Triangle
turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(100,50)
turtle.pendown()
turtle.circle(40,steps=3)
turtle.showturtle()

# Make Rectangle
turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(150,50)
turtle.pendown()
turtle.circle(40,steps=4)
turtle.showturtle()

# Make Pentagon
turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(200,50)
turtle.pendown()
turtle.circle(40,steps=5)
turtle.showturtle()

#Make circle
turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(200,50)
turtle.pendown()
turtle.circle(40)
turtle.showturtle()
turtle.done()


#Question No.2
x1=eval(input("enter x1:"))
y1=eval(input("enter y1:"))
x2=eval(input("enter x2:"))
y2=eval(input("enter y2:"))


distance=((x2-x1)**2+(y2-y1)**2)**0.5
turtle.penup()
turtle.goto(x1,y1)
turtle.write("P1")
turtle.pendown()
turtle.goto(x2,y2)
turtle.write("P2")
turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write(distance)
turtle.hideturtle()
turtle.showturtle()
turtle.done()

 #Question No.3
x1, y1 = eval(input("Enter center x1, y1: "))
x2, y2 = eval(input("Enter x, y of P1: "))
r = eval(input("Enter radius: "))

# Distance formula
d=((x1-x2)**2+(y1-y2)**2)**0.5

# Draw circle
turtle.pensize(3)
turtle.color("red")
turtle.penup()
turtle.goto(x1,y1-r)   # Move to bottom of circle
turtle.pendown()
turtle.circle(r)

# Draw point P1
turtle.penup()
turtle.goto(x2, y2)
turtle.dot(6, "purple")
turtle.write(" P1")

# Check condition
turtle.penup()
turtle.goto(150, 150)

if d <= r:
    turtle.write("Point P1 is inside", font=("Times", 18, "bold"))
else:
    turtle.write("Point P1 is outside", font=("Times", 18, "bold"))

turtle.hideturtle()
turtle.done()
#Question No.4
class Dog:
    attr1="Mammal"
    attr2="Dog"

    def fun(self):
       print("I am ,",self.attr1)
       print("I am ,",self.attr2)


Rogue=Dog()
print(Rogue.attr1)
Rogue.fun()

 #Question No.5
class circle:
    def __init__(self,r=100,s=10,t=40):
        self.x=r
        self.y=s
        self.radius=t
    def drawCircle(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.done()
a=circle()
a.drawCircle()
# #Question No.6
def __init__(self):
    print("employee created")
def __del__(self):
    print("Destructor called.Circle is deleted")
obj=circle()
del obj