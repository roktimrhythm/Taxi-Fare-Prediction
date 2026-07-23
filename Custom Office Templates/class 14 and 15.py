def greet():
    print("hello student")
greet()

# Types of Functions
# There are mainly 4 types.
# def means define a function.

# 1.No argument, no return

def hello():
    print("Hello")
hello()
# 2.function with arguments

def greet(name):
    print('hello',name)

greet("Rhythm")

def goodbye(actor):
    print("best of luck", actor)

goodbye("Paul Walker")

#Function With return

def add(a,b):
    return a+b

result = add(4343,434)

print(result)
# Difference Between Print and Return 
def add(a,b):
    print(a+b)

result = add(5,3)

print(result)

# Argument with return

def add(a,b):
    return a+b
#No argument but return
def give_number():
    return 10


# hard examples of function

# আমরা সবগুলোর square বের করবো।

def square_list(numbers):
    result = []

    for num in numbers:
        result.append(num*num)
    return result

data = [2,3,4,5]

print(square_list(data))

# 5️. Arguments এর Types

#1️. Positional argument

def greet(name,age):
    print(name,age)

greet("Rahim",30)

# 2️. Keyword argument

greet(age=20, name="Rhythm")

# 3.Keyword argument


def greet(name="guest"):
    print("how are you",name)

greet()
#Class কি

#Class হলো একটি blueprint বা template।

#মানে class নিজে কোনো বাস্তব জিনিস না, কিন্তু এটা দিয়ে আমরা বাস্তব object বানাতে পারি।

class Car:

    def start(self):
        print("car started")

#3️. self কি

class student:
    def show_name(self,name):
        print("student's name is",name)

s1 = student()
s1.show_name("Rhythm")

# normal
class website:
    def login(self, name, password, mobile_number):
        print("Account Details:")
        print("Name:",name)
        print("Password:",password)
        print("Mobile number:",mobile_number)

log1 = website()
log1.login("Rhythm",243343,345554)

# advanced

class Website:
    def login(self,name,password,mobile_number):
        
        print("------Account Details------")
        print(f"Name          :{name}")
        print(f"Password      :{password}")
        print(f"Mobile Number :{mobile_number}")
        
log1 = website()

log1.login("Rhythm",234345,87699786)


# lets make a mini project

class Website:

    def __init__(self,name,password,mobile_number):
        self.name = name
        self.password = password
        self.mobile_number = mobile_number

    def show_details(self):
        print("-----Account Details------")
        print("Name", self.name)
        print("Password", self.password)
        print("Mobile Number",self.mobile_number)
        print("---------------------------")
    
    def login(self, input_password):

        if input_password == self.password:
            print("Login successful")
        else:
            print("wrong password") 

# object create
user1 = Website("Rhythm",12345,987654321)
# show details
user1.show_details()
# login attempt
user1.login(12345)
'''
# Real OOP Project: Bank Account System

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(f"{self.name}'s Balance: {self.balance}")
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposit successfully")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")

        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

acc1 = BankAccount("Rhythm",15000)
acc1.show_balance()

acc1.deposit(7800)

acc1.withdraw(20000)

acc1.show_balance()

'''
# new project

class BankAccount:
    def __init__ (self,name,balance):
        self.name = name
        self.balance = balance
    
    def show_balance(self):
        print(f"{self.name}'s balance: {self.balance}")

    def deposit(self,amount):
        if amount > 0:
           self.balance += amount
           print(f"{amount} deposited successfully")
        else:
             
             print(" Invalid deposit amount")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insuficient balance")
        
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")

    def transfer(self, other_account, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        self.balance -= amount
        other_account.balance += amount
        print("Transfer successful")


acc1 = BankAccount("Rhythm",50000)
acc2 = BankAccount("Rahim",30000)

acc1.show_balance()
acc2.show_balance()

acc1.deposit(50000)
acc1.withdraw(30000)

acc1.transfer(acc2,10000)

acc1.show_balance()
acc2.show_balance()

# new project
# Project: Student Management System

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def show_details(self):
        print(f"{self.name} marks: {self.marks}")

    def add_marks(self,amount):
        if amount > 0:
            self.marks += amount
            print(f"{amount} marks has increased")
        else:
            print("invalid marks")
    
    def grade(self):
        if self.marks >= 90:
            print("A")

        
        elif self.marks >= 80:
            print("B")

        elif self.marks >= 70:
            print("C")

        else:
            self.marks < 70
            print("Fail")

    def compare(self,other_student):

        if self.marks > other_student.marks:
            print(self.name, "has higher marks")
        elif self.marks < other_student.marks:
            print(other_student.name, "has higher marks")
        else:
            print("both have equal marks")
s1 = student("Rhythm",95)
s2 = student("Alex",67)

s1.show_details()
s2.show_details()

s1.grade()
s2.grade()

s1.compare(s2)

s2.add_marks(20)
s2.show_details()
s2.grade()

# Problem: Simple Banking System (Advanced Practice)

print("\nSimple Banking System")

# Parent class

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # 🔒 encapsulation
        
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit successfully")
        else:
            print("Invalid deposit amount")

    def withdraew(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdraw successfully")

    def get_balance(self):
        return self.__balance




            
                


        


        


