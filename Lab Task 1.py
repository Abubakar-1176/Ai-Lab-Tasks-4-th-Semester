# Two Questions
x=9
if x > 0:
  if x > 10:
    print("large")
  print("positive")
print("done")  

# slide no 18
age = 45
salary = 1456.5
name = "abubakar"
print(age)
print("salary=",salary)
print("name=",name)
# slide no 20
name = input("Enter your name:")
age = int(input("Enter your age:"))
salary = float(input("Enter your salary:"))
print(type(name))
print(type(age))
print(type(salary))

#slide no 22
x = "abubakar zafar"
print("Complete name:",x)
print("index string:",x[0])
print("Complete name:",x[-5])
print("Complete name:",x[0:8])
print("Complete name:",x[-8:1])
print("Complete name:",x[:8])

#slide no 23
print(x.strip())
print(x.lower())
print(x.upper())
print(x.replace("b","j"))

#slide no 29
a=13
b=33
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
 
#slide no 32 
print("a=",bin(a),"\nb=",bin(b)) 
print("a&b=",bin(a&b))
print("a|b=",bin(a|b))
print("a^b=",bin(a^b))
print("a|b=",bin(a|b))
print("~a=",bin(~a))
print("a<<2=",bin(a<<2))
print("a>>b=",bin(a>>2))

#slide no 39
w = 55
y = 100
if w > y:
  print("w is greater than y")
  
if y > w:
  print("y is greater than w")
  
  print("Y")
  
def add(x,y,z=0):
  print(x+y+z)
def mul(x,y,z=1):
  print(x*y*z)
def div(x,y,z=1):
  print(x//y//z)
  
  
add(10,20,30)
mul(10,20,30)
div(10,20,2)  