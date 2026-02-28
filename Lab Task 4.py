print("***************** Lab Task 4 : Operator Overloading *****************")
print(" Question no.1 :")
class Add:
  def __init__(self,a):
    self.a=a
    
  def __add__(self,other):
    return self.a+other.a
        
obj1=Add(10)
obj2=Add(20)
print(obj1+obj2)
obj3=Add("Abubakar")
obj4=Add("Zafar")
print(obj3+obj4)

print(" ****************** Question no.2 : ******************** ")
class A:
  def __init__(self,a):
    self.a=a
    
  def __lt__(self,other):
    if(self.a<other.a):
      return "Less than"
    else:      return "Greater than"
    
  def __eq__(self,other):
    if(self.a==other.a):
      return "Both are equal"
    else:      return "Both are not equal"
        
obj1=A(10)
obj2=A(20)
print(obj1<obj2)
print(obj1==obj2) 

print(" ****************** Question no.3 : ********************")  
class Person:
  def __init__(self,fname,lname):
    self.fname=fname
    self.lname=lname
    
  def printname(self):
    print(self.fname,self.lname)
class Student(Person):
 pass
x=Student("Abubakar","Zafar")
x.printname()    

print(" ****************** Question no.4 : ********************")
class Person:
  def __init__(self,fname,lname):
    self.fname=fname
    self.lname=lname
    
  def PrintNametname(self):
    print(self.fname,self.lname)
class Student(Person):
  def __init__(self,fname,lname,rollno):
    super().__init__(fname,lname)
    self.rollno=rollno
  def welcome(self):
    print("Welcome",self.fname,self.lname,"Roll No:",self.rollno)  
 
x=Student("Abubakar","Zafar",1176)
x.PrintNametname()  
x.welcome()
print(" ******************************* Question No.5 : *******************************")
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastnaem=lname
    def printname(self):
        print(f"Person name:{self.firstname}{self.lastnaem}")
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def printname(self):
        super().printname()
        print(f"student graduation year:{self.graduationyear}")
x=student("Abubakar","Zafar",2028)
x.printname()
  