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

# ADVANCED FOR LOOP PRACTICE

# Problem 1: Index + Value + Condition (enumerate)

Apps = ["facebook","instragram","youtube","whatsapp","massanger","yahoo"]

if "chatgpt" in Apps:
    print("yes")
else:
     print("chatgpt is not an app its a chatbot")
     
for i, App in enumerate(Apps, start=1):
     print(i,App)

# Problem 2: Sum of Even Numbers (range)

total = 0
'''
for i in range(1,21):
    if i % 2 == 0:
        total += i

print("sum of even numbers:", # total) this was harder
'''

total = 0 
for i in range(2,2534,8):
    total += i
print("sum of even numbers",":", total)

# Problem 3: Character Frequency (String Loop)
#  Count each character

word = "supercalifrazilisticexpialiducious"

for char in word:
    print(char, "appears", word.count(char), "times")
    
# Problem 4: Dictionary Loop (IMPORTANT 🔥)

player = {
    "name": "Randy Orton",
    "age": "44",
    "company": "WwE",
    "finishing move": "RKO",
    "titles": "14 time wwe champion"

}

for key, value in player.items():
    print(key, ":", value)

# Problem 5: Reverse List (Without reverse())

numbers = [12,3223,33,45,43]

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])

# Problem 6: Find Common Elements (Loop + Condition)

a = [2342,4354,324,34243]
b = [2342,3432,324,324,4242]

for num in a:
    if num in b:
        print(num)


# Problem 7: Multiplication Table (User Input)
'''
num = int(input("enter number:"))

for i in range(1,11):
    print(num, "x", i, "=", num*i)
    '''

# Problem 8: Remove Duplicates (Loop Logic)

numbers = [122334,323,233,233,3434,3434,645,645,545]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

# while loop

# 1. While Loop with Condition

num = 10
while num > 0:
    print(num)
    num -= 1

# 2.While Loop with STRING (IMPORTANT 🔥)

text = "obnocxious"
i = 0
while i < len(text):
    print(text[i])
    i += 1

# 3. While Loop with LIST

fruits = ["apple","mango","banana"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# 4. BREAK (Stop Loop Early)

i = 1
''''
while i <= 10:
    if i == 8:
        break
    print(i)
    i += 1
'''
# 5. CONTINUE (Skip Step)

while i < 15:
    i += 1
    if i == 5:
        continue
    print(i)

# 6. Real-Life Example (Login System)
'''
password = ""

while password != "122234":
    password = input("enter password: ")

print("access granted")
'''
