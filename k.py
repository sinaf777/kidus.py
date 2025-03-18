#  print formating

name = 'blackie'
age = 25
p_language= 'python'
print(f'My name is {name}.')
print(f'I am {age} years old :)')
print(f'I love {p_language} programming!')

#  swapping variables
x,y=2,3
x,y=y,x
print(x)
print(y)

#  simple calculator

print('=================================')
print('        WELCOME')
print('=================================')
a=float(input('Enter first number: '))
b=float(input('Enter second number: '))
opp=input('Choose an opretor (+, -, *, /)')
if opp == '+':
    print(f'Result = {a+b}')
elif opp == '-':
     print(f'Result = {a-b}')
elif opp == '*':
     print(f'Result = {a*b}')
elif opp == '/':
   if b==0:
            print('Undefined (can not be devided by zero).')
   else:
            print(f'Result = {a/b}')
else:
     print('Invalid input TRY AGIAN!!')

#  type

X = 10
Y = 3.14
Z = "HUISA"
A = True
print(type(X), type(Y), type(Z), type(A))

#  list oprations 

list = [2, 4, 6, 8, 10]
list.append(0)
list.remove(4)
print(f'Max: {max(list)}, Min: {min(list)}')

#  Dictionary manipulation

students = {'abebe':15, 'hiwot':19}
students['meseret']=99
students['abebe']=9
del students['hiwot']
print(students)

#  tuple unpacking

ddd = (10, 20, 30)
a, b, c = ddd
print(a, b, c)

#  sum of even numbers 1 - 100

sum = sum(i for i in range (1,101) if i % 2 == 0)
print(f'sum of even number 1 - 100 = {sum}')

#  n factorial

def fac(n):
      e = 1
      for i in range(1, n+1):
            e *=i
            return e
print(f'Factor of 5 is : {fac(5)}')

#  Multiplication Table

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
multiplication_table(5)

#  Reverse a String

def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
print(reverse_string("Python"))

#  Fibonacci Sequence

def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
print(fibonacci(10))

#  Count Digits in a Number

def count_digits(n):
    return len(str(abs(n)))
print(count_digits(12345))

#  Prime Number Check

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(29))

#  Finding Common Elements

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = list(set(list1) & set(list2))
print("Common Elements:", common_elements)

#  Student Class

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Course: {self.course}")

#  Inheritance

class Course:
    def get_details(self):
        print("This is a general course.")
class WebDevClass(Course):
    def get_details(self):
        print("This is a Web Development course.")

#  Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")
    def get_balance(self):
        return self.__balance

#  Polymorphism
class Car:
    def move(self):
        print("The car is moving fast")
class Bike:
    def move(self):
        print("The bike is moving slowly")
def vehicle_move(vehicle):
    vehicle.move()
