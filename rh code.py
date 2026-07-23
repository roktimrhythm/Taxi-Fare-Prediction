print("hello")

#list

# 1.append

names = ["appale","guava","sugar cane","lichi"]
names.append("banana")
print(names)

# 2.extend

a = [233,344,6763,877,]
b = [232,232,2332,233]
a.extend(b)
print(a)

# 3.insert

a = [2323,4344,55443,34,22]
a.insert(2323,244)
print(a)
Actors = ["tom cruss","leonardo","jorge clooney"]
Actors.insert( 2,"henry cavill",)
print(Actors)

# 4.remove 
# it works only with value

colors = ["red","blue","green"]

colors.remove("blue")

print(colors)

radiation = [2.4,23,3.3,33]
radiation.remove(2.4)
print(radiation)

# 5.pop

nums = [232,3233,233,2334]
nums.pop(3)
print(nums)

institutions = ["creative it","mentors","saifurs"]
institutions.pop(2)
print(institutions)

# 6.clear

data = [322,32434,434]
data.clear()
print(data)

# 7.index

cause = ["accident","run over","hit and run","fell down"]
print(cause.index("run over"))
print(cause)

# 8.count

numbers = [324,3434,3434,3434]
print(numbers.count(3434))
print(numbers)

# 9.sort

nums = [4,3,6,66]
nums.sort()
print(nums)

# another example

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)

# 10.reverse 

items = [22,34,23]
items.reverse()
print(items)

# 11.copy

a = [12,323,45]
b = a.copy()
print(b)



#else,elif,else statements

#if and else

age = 17
if age >= 18:
    print("you can vote")
else:
    print("you cant vote")    

 ##list

# 1.append

names = ["appale","guava","sugar cane","lichi"]
names.append("banana")
print(names)

# 2.extend

a = [233,344,6763,877,]
b = [232,232,2332,233]
a.extend(b)
print(a)

# 3.insert

a = [2323,4344,55443,34,22]
a.insert(2323,244)
print(a)
Actors = ["tom cruss","leonardo","jorge clooney"]
Actors.insert(3, "henry cavill")
print(Actors)

# 4.remove 


colors = ["red","blue","green"]

colors.remove("blue")

print(colors)

radiation = [2.4,23,3.3,33]
radiation.remove(2.4)
print(radiation)

# 5.pop

nums = [232,3233,233,2334]
nums.pop(3)
print(nums)

institutions = ["creative it","mentors","saifurs"]
institutions.pop(2)
print(institutions)

# 6.clear

data = [322,32434,434]
data.clear()
print(data)

# 7.index

cause = ["accident","run over","hit and run","fell down"]
print(cause.index("run over"))
print(cause)

# 8.count

numbers = [324,3434,3434,3434]
print(numbers.count(3434))
print(numbers)

# 9.sort

nums = [4,3,6,66]
nums.sort()
print(nums)

# 10.reverse 

items = [22,34,23]
items.reverse()
print(items)

# 11.copy

a = [12,323,45]
b = a.copy()
print(b)


#else,elif,else statements

marks = 60   

if marks >= 90:
    print("you got A grade")
elif marks >= 80:
    print("you got b grade")
elif marks >= 70:
    print("you got c grade")
else:
    print("you have to study more")    

# else,elif,else statements

balance = 6000
withdraw = 4000

if withdraw > balance:
    print('insufficient balance')
elif withdraw <= balance:
    balance = balance - withdraw    
    print("withdrawal successful")
    print('Remaining balance:',balance)
else:
    print("Invalid amount")

#else,elif,else statements
'''
username = "admin"
password = "34434"
blocked = False

user = input("Enter username:")
passw = input('Enter password:')

if user == username and passw == password and not blocked:
    print("Login successful")
elif user == username and passw != password:
    print("Wrong password")

elif user != username:
    print("User not found")

else:
    print("Account blocked")
'''

#class 4 
# learn various concepts and methods in string

# 1. indexing
'''
text = "python"
print(text[0])
print(text[1])
print(text[-1])

email = "student@gmail.com"
print(email[0])
print(email[1])
print(email[2])
print(email[3])
'''

# .2 slicing

website = "www.google.com"

print(website[4:10])  # google
print(website[:3])    # www
print(website[-3:])   # com

Social_media ="facebook,instragram,youtube"
print(Social_media[0:8])
print(Social_media[9:19])
print(Social_media[20:27])

# 3.replace

message = "I hate bugs"
print(message)
new_message = message.replace("hate","love")
print(new_message)

# 4.split

sentence = "Python is very powerful"
words = sentence.split()
print(words)

# another example

data = "Dhaka-Chittagong-Sylhet"
cities = data.split("-")
print(cities)

# 5.join

items = ["rice","fish","vegetables","meat"]
meal = ", ".join(items)
print(meal)

# another example

countries_that_have_nuclear_weapons = ["Usa","Russia","China","Uk","India","Pakistan",'France',"North korea"]
fire_index = ", ".join(countries_that_have_nuclear_weapons )
print(fire_index)

fruits = ["apple","banana","mango"]
salad = "/".join(fruits)
print(salad)

# 6.title

book = "the power of habit"
print(book.title())

# 7.upper and lower

username = "Roktim Rhythm"
print(username.lower())
print(username.upper())

# 8.count

text = "Mississippi"
print(text.count("s"))
print(text.count("i"))

# class 5 
# part 1.tuple
# learn various concepts and methods in tuple 

# 1.slicing

numbers = (234,45,344,455)

print(numbers[1:4])
print(numbers[:3])

# 2. immutable
#numbers = (23,43,34)
#numbers[2] = 233
# unchangeable

# 3. convert tuple to list

numbers = (234,34,45)
num_list = list(numbers)
print(num_list)

words = ("Apple","banana","orange")
words_list = list(words)
print(words_list)

# 4. Modify tuple(using list) + list to tuple

words = ("monkey","bear","tiger","lion")
words_list = list(words)
print(words_list)

words_list[1] = "dear"
words = tuple(words_list)
print(words)

my_list = [1, 2, 3]

my_tuple = tuple(my_list)

print(my_tuple)  

# part 2.set

# 1. Unorderd
my_set = {"apple", "banana", "mango"}
print(my_set)

# 2.adding elements

my_set = {876, 66, 666}

my_set.add(8775)

print(my_set)

# 3.removing elements

my_set.discard(8775)

print(my_set)

# 4.union(combine sets)
a = {24, 232, 321}
b = {234, 34, 233}
print(a.union(b))

# 5. intersection

a = {344,345,347}
b = {344,345,766}

print(a.intersection(b))

# 6.diference

a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))

# 7.unique elements
numbers = {4535,5454,545,545}
unique = set(numbers)
print(unique)

# 8.common elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = set(list1).intersection(set(list2))

print(common)

# Dictionary in python

# 1.Key value relationship

student = {
     "name": "Rahim",
     "age": 34 
}
print(student["name"])
print(student["age"])

Player = {
     "name": "Ronaldo",
     "Brand": "Adidas",
     
     "Age": 40,
     "Sports": "Football",
     "Position": "forward",

}
print(Player["name"])
print(Player["Brand"])
print(Player["Age"])
print(Player["Sports"])
print(Player["Position"])

# another example

App = {
    "name": "facebook",
    "inventor": "mark jukerburg",
    "year of invention": 2003,
    "partners": 2,
    "users": "only americans"

}
for key,value in App.items():
    print(key, ":", value) # this is a technic to do it faster

# 2.unique keys+items+adding data



Meta = {
    "name": "facebook",
    "inventor": "mark jukerburg",
    "year of invention": 2003,
    "partners": 2,
    "users": "only americans"

}
Meta["age of jukerburg"] = 23 # add method

del Meta["age of jukerburg"] # removing data

print(Meta.items())

# 3.loop through dictionary

Meta = {
    "name": "facebook",
    "inventor": "mark jukerburg",
    "year of invention": 2003,
    "partners": 2,
    "users": "only americans"

}

for key, value in Meta.items():
    print(key, ":",value)

# 4.cheack if key exists

if "age" in Meta:
    print("yes")
else:
    print("age is 23")

'''
# class 7
#for loop and while loop
# 1.for loop

for i in range(9):
    print(i)

# for loop with list

fruits = ["apple","orange","guava","mango","jackfruit"]

for fruit in fruits:
    print(fruit)

#Best Method: enumerate() (VERY IMPORTANT)

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

for i, fruit in enumerate(fruits, start=1):
    print("number", i, ":",fruit)
'''