# Practice 1 — Prime Number Function
'''
def is_prime(num):

    for i in range(2, num):

        if num % i == 0:
            print("not prime")
        return
    print("prime number")

is_prime(7)
is_prime(8)
'''     
'''  
def is_prime(num):

    if num <= 1:
        print("Not prime")
        return

    for i in range(2, num):

        if num % i == 0:
            print("Not prime")
            return

    print("Prime number")

is_prime(9)
'''

def is_prime(num):
    if num <= 15:
        print("it a prime numbere")
        return
        for i in range(2,num):

            if num % i == 0:
             print("its not a prime number")

is_prime(12)

def is_prime(num):

    for i in range(2, num):

        if num % i == 0:
            print("its not prime number")
            return

    print("its a prime number")


is_prime(12)

def factorial(num):

    result = 1

    for i in range(1,num+1):
        result = result * i

    return result

print(factorial(5))


# Practice 3 — Count Vowels

def count_vowels(text):

    vowels = "aeiou"
    count = 0

    for chr in text:

        if chr in vowels:

            count += 1

    return count

print(count_vowels("banana"))

# Practice 4 — Largest Number in List

def find_max(numbers):

    maximum = numbers[0]

    for num in numbers:

        if num > maximum:

            maximum = num

    return maximum

data = [3234,443,455,233,345,243332]


print(find_max(data))

# Bonus — Mini Calculator

def calculator(a,b, operator):

    if operator == "+":
        return a-b
    
    elif operator == "-":
        return a-b
    
    elif operator == "*":

        return a*b
    
    elif operator == "/":
        return a/b
    
    else:

        return "imvalid operator"
    
print(calculator(10,5,"+"))
print(calculator(10,5,"*"))
    