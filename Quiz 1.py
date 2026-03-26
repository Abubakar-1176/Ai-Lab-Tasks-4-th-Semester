
print("****************** Quiz No.1*****************")
# print("-------Q.1: Celsius to Fahrenheit-------")
# celsius = float(input("Enter a degree in Celsius: "))
# fahrenheit = (9/5) * celsius + 32
# print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")

# print("\n-------Q.2: Cylinder Volume and Area-------")
# length = int(input("Enter the length of a cylinder: "))
# radius = int(input("Enter the radius of a cylinder: "))
# area = radius * radius * 3.14
# volume = area * length
# print(f"The area is {area}")
# print(f"The volume is {volume}")

# print("\n-------Q.3: Employee Payroll Calculator-------")
# name = input("Enter employee's name: ")
# hours = float(input("Enter number of hours worked in a week: "))
# pay_rate = float(input("Enter hourly pay rate: "))
# fed_tax = float(input("Enter federal tax withholding rate: "))
# state_tax = float(input("Enter state tax withholding rate: "))
# gross_pay = hours * pay_rate
# fed_withholding = gross_pay * fed_tax
# state_withholding = gross_pay * state_tax
# total_deduction = fed_withholding + state_withholding
# net_pay = gross_pay - total_deduction
# print(f"Employee Name: {name}")
# print(f"Hours Worked: {hours}") 
# print(f"Pay Rate: ${pay_rate}")
# print(f"Gross Pay: ${gross_pay}")
# print(f"Deductions:")
# print(f"  Federal Withholding ({fed_tax*100}%): ${fed_withholding}")
# print(f"  State Withholding ({state_tax*100}%): ${state_withholding}")
# print(f"  Total Deduction: ${total_deduction}")
# print(f"Net Pay: ${net_pay}")

# print("\n-------Q.4: Future Investment Value    -------")
# investment = float(input("Enter investment amount: "))
# annual_rate = float(input("Enter annual interest rate: "))
# years = int(input("Enter number of years: "))
# monthly_rate = annual_rate / 1200
# months = years * 12
# future_value = investment * (1 + monthly_rate) ** months
# print(f"Future Investment Value: ${future_value}")  


print("\n-------Q.5:  Point Inside Circle and Rectangle Check -------")
#rite a Python program that asks the user to enter a point (x, y). 
# Check whether the point lies inside a circle centered at (0, 0) with radius 10, 
# and inside a rectangle centered at (0, 0) with width 10 and height 5. 
# Print a message for each case. 
# Expected output / sample: 
# Enter point x: 4 
# Enter point y: 3 
# Point (4, 3) is inside the circle. 
# Point (4, 3) is inside the rectangle
x=int(input("Enter x for center: "))
y=int(input("Enter y for center: "))
x1=int(input("Enter x for point: "))
y1=int(input("Enter y for point: "))
radius=10
distance=((x-x1)**2+(y-y1)**2)**0.5
if distance<radius:
    print("Point (x1, y1) is inside the circle.")
elif distance>radius:
    print("Point (x1, y1) is outside the circle.")
else:    print("Point (x1, y1) is on the circle.")

#Create a class called Book with the following attributes: ISBN, Title, Price, Main Area, Sub Area, 

print("\n-------Q.6:  Book Class -------")
class Book:
    def __init__(self, ISBN, Title, Price, Main_Area, Sub_Area, No_of_Pages):
        self.ISBN = ISBN
        self.Title = Title
        self.Price = Price
        self.Main_Area = Main_Area
        self.Sub_Area = Sub_Area
        self.No_of_Pages = No_of_Pages

    def show(self):
        print(f"ISBN: {self.ISBN}")
        print(f"Title: {self.Title}")
        print(f"Price: ${self.Price}")
        print(f"Main Area: {self.Main_Area}")
        print(f"Sub Area: {self.Sub_Area}")
        print(f"No of Pages: {self.No_of_Pages}")

book1 = Book("978-0134685991", "Introduction to Ai", 129.99, "Computer Science", "Algorithms", 1200)
book2 = Book("978-0134685992", "Software Construction and Design", 59.99, "Computer Science", "Software Engineering", 1176)
book1.show()
book2.show()

print("\n-------Q.7:  Loan Class -------")
class Loan:
    def __init__(self,annualRate,years,loanAmount):
        self.__annualRate=annualRate
        self.__years=years
        self.__loanAmount=loanAmount
    def getMonthlyPayment(self):
        monthlyRate = self.__annualRate/1200
        return self.__loanAmount*monthlyRate/(1-(1+monthlyRate)**(-self.__years*12))
    def getTotalPayment(self):
        return self.getMonthlyPayment()*self.__years*12
l1 = Loan(5, 1, 1000)
print("Monthly Payment:",l1.getMonthlyPayment())
print("Total Payment:",l1.getTotalPayment())

print("\n-------Q.8: BMI Class -------")
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


print("\n-------Q.9: Operator Overloading  Complex Numbers -------")
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = Complex(11,76)
c2 = Complex(76,11)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)

