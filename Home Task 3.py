# print("Home Task 3 Q.1 -Draw a rectangle ")
# import turtle as t
# def draw_rectangle(width,height,x,y):
#     t.penup()
#     t.goto(x,y)  
#     t.pendown()
#     for i in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)
# draw_rectangle(150,100,-50,-50)
# t.done()
# print("Home Task 3 Q.2 ")
import turtle as t
import math
t.speed(0)
t.hideturtle()
t.penup()
t.goto(-400,0)
t.pendown()
t.goto(400,0)
t.penup()
t.goto(0,-300)
t.pendown()
t.goto(0,300)
rect_center_x=-200
rect_center_y=0
width=200
height=120
t.penup()
t.goto(rect_center_x - width/2, rect_center_y - height/2)
t.pendown()
for i in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
circle_center_x=200
circle_center_y=0
radius = 100
t.penup()
t.goto(circle_center_x, circle_center_y - radius)
t.setheading(0)
t.pendown()
t.circle(radius)
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
t.penup()
t.goto(x, y)
t.dot(10, "red")
if (rect_center_x - width/2 <= x <= rect_center_x + width/2) and \
   (rect_center_y - height/2 <= y <= rect_center_y + height/2):
    print("Point is inside the rectangle.")
else:
    print("Point is outside the rectangle.")
distance = math.sqrt((x - circle_center_x)**2 + (y - circle_center_y)**2)
if distance <= radius:
    print("Point is inside the circle.")
else:
    pritn("Point is outside the circle.")
t.done()
# import turtle as t
# import math
# t.speed(0)
# t.hideturtle()
# t.penup()
# t.goto(-400, 0)
# t.pendown()
# t.goto(400, 0)
# t.penup()
# t.goto(0, -300)
# t.pendown()
# t.goto(0, 300)
print("----- RECTANGLES -----")
x1 = float(input("Rect1 center x: "))
y1 = float(input("Rect1 center y: "))
w1 = float(input("Rect1 width: "))
h1 = float(input("Rect1 height: "))
x2 = float(input("Rect2 center x: "))
y2 = float(input("Rect2 center y: "))
w2 = float(input("Rect2 width: "))
h2 = float(input("Rect2 height: "))
def draw_rectangle(cx, cy, w, h, color):
    t.penup()
    t.goto(cx - w/2, cy - h/2)
    t.setheading(0)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
draw_rectangle(x1, y1, w1, h1, "blue")
draw_rectangle(x2, y2, w2, h2, "red")
left1, right1 = x1 - w1/2, x1 + w1/2
bottom1, top1 = y1 - h1/2, y1 + h1/2
left2, right2 = x2 - w2/2, x2 + w2/2
bottom2, top2 = y2 - h2/2, y2 + h2/2
if left2 >= left1 and right2 <= right1 and bottom2 >= bottom1 and top2 <= top1:
    rect_result = "Rectangle 2 is inside Rectangle 1"
elif right2 > left1 and left2 < right1 and top2 > bottom1 and bottom2 < top1:
    rect_result = "Rectangles Overlap"
else:
    rect_result = "Rectangles Do Not Overlap"
print(rect_result)
# print("\n----- CIRCLES -----")
# cx1 = float(input("Circle1 center x: "))
# cy1 = float(input("Circle1 center y: "))
# r1 = float(input("Circle1 radius: "))
# cx2 = float(input("Circle2 center x: "))
# cy2 = float(input("Circle2 center y: "))
# r2 = float(input("Circle2 radius: "))
# def draw_circle(cx,cy,r,color):
#     t.penup()
#     t.goto(cx,cy-r)
#     t.setheading(0)
#     t.pendown()
#     t.color(color)
#     t.circle(r)
# draw_circle(cx1, cy1, r1,"green")
# draw_circle(cx2, cy2, r2,"purple")
# distance=math.sqrt((cx2-cx1)**2+(cy2-cy1)**2)
# if distance+r2<=r1:
#     circle_result="Circle 2 is inside Circle 1"
# elif distance<r1+r2:
#     circle_result="Circles Overlap"
# else:
#     circle_result="Circles Do Not Overlap"
# print(circle_result)
# t.penup()
# t.goto(-380,-270)
# t.write(rect_result)
# t.goto(-380,-290)
# t.write(circle_result)
# t.done()
# # QUESTION NO 04:
# class Book:
#     def __init__(self,ISBN,title,price,main_area,sub_area,pages):
#         self.ISBN=ISBN
#         self.title=title
#         self.price=price
#         self.main_area=main_area
#         self.sub_area=sub_area
#         self.pages=pages
#     def display(self):
#         print("ISBN:",self.ISBN)
#         print("Title:",self.title)
#         print("Price:",self.price)
#         print("Main Area:",self.main_area)
#         print("Sub Area:",self.sub_area)
#         print("Pages:",self.pages)
# b1 = Book("12345","Python Basics",500,"Programming","Python",300)
# b1.display()
# # Question no 05
# class Computer:
#     def __init__(self,brand,name,speed,memory,size):
#         self.brand=brand
#         self.name=name
#         self.speed=speed
#         self.memory=memory
#         self.size=size
#     def display(self):
#         print("Brand:",self.brand)
#         print("Name:",self.name)
#         print("Speed:",self.speed)
#         print("Memory:",self.memory)
#         print("Size:",self.size)
# c1 = Computer("Dell",".Inspiron","3.2GHz","8GB","15 inch")
# c1.display()
# class Loan:
#     def __init__(self,annualRate,years,loanAmount):
#         self.__annualRate=annualRate
#         self.__years=years
#         self.__loanAmount=loanAmount
#     def getMonthlyPayment(self):
#         monthlyRate = self.__annualRate/1200
#         return self.__loanAmount*monthlyRate/(1-(1+monthlyRate)**(-self.__years*12))
#     def getTotalPayment(self):
#         return self.getMonthlyPayment()*self.__years*12
# l1 = Loan(5, 1, 1000)
# print("Monthly Payment:",l1.getMonthlyPayment())
# print("Total Payment:",l1.getTotalPayment())
# # Question no 07:
class BMI:
    def __init__(self,name,age,weight,height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def getBMI(self):
        return self.weight/(self.height**2)
    def getStatus(self):
        bmi=self.getBMI()
        if bmi<18.5:
            return"Underweight"
        elif bmi<25:
            return"Normal"
        elif bmi<30:
            return"Overweight"
        else:
            return "Obese"
p1 = BMI("Abubakar Zafar",20,60,1.7)
print("BMI:",p1.getBMI())
print("Status:",p1.getStatus())