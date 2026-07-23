for i in range(1,11):
    print(f' {40} x {i} = {40*i}')

for i in range(1,11):
    print(f" {50} + {i} = {50+i}")

for i in range(1,11):
    print(f" {70} / {i} = {76/i}")

for i in reversed(range(1, 11)):
    print(i)

# 1.method   

print("\nRight Side Pyramid")

for i in range(10):
    x = "*"
    x = x * i
    print(f'{x:>25}')

# 2.method

rows = 10

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

n = 7
for i in range(1,n):

    print(" "* i(n-1) + "* "*i)