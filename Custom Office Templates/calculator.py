print("========== Calculator ==========")


# -------- Functions --------
def addi(a, b):
    return a + b


def subi(a, b):
    return a - b


def multi(a, b):
    return a * b


def divi(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


# -------- Main Function --------
def cal():
    while True:

        print("\n===== MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Calculator Closed Successfully!")
            break

        elif choice in ["1", "2", "3", "4"]:

            num1 = float(input("Enter the 1st number: "))
            num2 = float(input("Enter the 2nd number: "))

            if choice == "1":
                print("Result:", addi(num1, num2))

            elif choice == "2":
                print("Result:", subi(num1, num2))

            elif choice == "3":
                print("Result:", multi(num1, num2))

            elif choice == "4":
                print("Result:", divi(num1, num2))

        else:
            print("Invalid Choice! Please enter a number between 1 and 5.")


# -------- Run Program --------
cal()