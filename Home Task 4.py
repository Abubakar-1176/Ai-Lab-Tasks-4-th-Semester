print("__________________________ Question No.1_____________________")
class Loan:
    def __init__(self):
        self.__annualInterestRate = 2.5
        self.__numberOfYears = 1
        self.__loanAmount = 1000
        self.__borrower = ""
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def getNumberOfYears(self):
        return self.__numberOfYears
    def getLoanAmount(self):
        return self.__loanAmount
    def getBorrower(self):
        return self.__borrower
    def setAnnualInterestRate(self, rate):
        self.__annualInterestRate = rate
    def setNumberOfYears(self, years):
        self.__numberOfYears = years
    def setLoanAmount(self, amount):
        self.__loanAmount = amount
    def setBorrower(self, name):
        self.__borrower = name
    def getMonthlyPayment(self):
        monthlyInterestRate = self.__annualInterestRate / 1200
        monthlyPayment = (self.__loanAmount * monthlyInterestRate) / \
                         (1 - (1 / ((1 + monthlyInterestRate) ** (self.__numberOfYears * 12))))
        return monthlyPayment
    def getTotalPayment(self):
        return self.getMonthlyPayment() * self.__numberOfYears * 12
loan1 = Loan()
loan1.setBorrower("Muhammad Abubakar Zafar")
loan1.setLoanAmount(80000)
loan1.setNumberOfYears(3)
print("Monthly Payment:", loan1.getMonthlyPayment())
print("Total Payment:", loan1.getTotalPayment())

print("__________________________ Question No.2_____________________")
class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height
    def getBMI(self):
        return self.__weight / (self.__height ** 2)
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
person1 = BMI("Muhammad Abubakar Zafar", 22, 70, 2.75)
print("BMI:", person1.getBMI())
print("Status:", person1.getStatus())


print("__________________________ Question No.3 _____________________")
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

print("__________________________ Question No.4 _____________________")
import math
class RationalNumber:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero!")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        gcd = math.gcd(numerator, denominator)
        self.num = numerator // gcd
        self.den = denominator // gcd
    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return RationalNumber(num, den)
    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return RationalNumber(num, den)
    def __mul__(self, other):
        return RationalNumber(self.num * other.num,
                              self.den * other.den)
    def __truediv__(self, other):
        return RationalNumber(self.num * other.den,
                              self.den * other.num)
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den
    def __str__(self):
        return f"{self.num}/{self.den}"
r1 = RationalNumber(11, 76)
r2 = RationalNumber(76, 11)
print("Addition:", r1 + r2)
print("Subtraction:", r1 - r2)
print("Multiplication:", r1 * r2)
print("Division:", r1 / r2)

print("__________________________ Question No.5 _____________________")
class Polynomial:
    def __init__(self):
        self.terms = {}   
    def add_term(self, coefficient, exponent):
        if exponent in self.terms:
            self.terms[exponent] += coefficient
        else:
            self.terms[exponent] = coefficient
    def __add__(self, other):
        result = Polynomial()
        result.terms = self.terms.copy()
        for exp, coeff in other.terms.items():
            if exp in result.terms:
                result.terms[exp] += coeff
            else:
                result.terms[exp] = coeff
        return result
    def __sub__(self, other):
        result = Polynomial()
        result.terms = self.terms.copy()
        for exp, coeff in other.terms.items():
            if exp in result.terms:
                result.terms[exp] -= coeff
            else:
                result.terms[exp] = -coeff
        return result
    def __mul__(self, other):
        result = Polynomial()
        for exp1, coeff1 in self.terms.items():
            for exp2, coeff2 in other.terms.items():
                result.add_term(coeff1 * coeff2, exp1 + exp2)
        return result
    def __str__(self):
        result = ""
        for exp in sorted(self.terms.keys(), reverse=True):
            coeff = self.terms[exp]
            result += f"{coeff}x^{exp} + "
        return result[:-3]
p1 = Polynomial()
p1.add_term(2, 2)   
p1.add_term(3, 1)   
p2 = Polynomial()
p2.add_term(1, 2)   
p2.add_term(4, 0)   
print("Addition:", p1 + p2)
print("Subtraction:", p1 - p2)
print("Multiplication:", p1 * p2)
