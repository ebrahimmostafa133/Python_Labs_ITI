# ========================================
#                   Task1
# ========================================
while True:
    num = input("Enter a number: ")
    try:
        num = int(num)
        start = int(input("Enter the start: "))
        end = int(input("Enter the end: "))
        print(start <= num <= end)
        break
    except ValueError:
        print("Invalid input")
        continue

# ========================================
#                   Task2
# ========================================
while True:
    age = input("Enter your age: ")
    coupon = input("Do you have a coupon? (yes/no): ")
    try:
        age = int(age)
        if age < 18 or age > 65 or coupon == "yes":
            print("Eligible for discount")
        else:
            print("Not eligible for discount")
        break
    except ValueError:
        print("Invalid input")
        continue

# ========================================
#                   Task3
# ========================================
name = input("Enter your name: ")
print(f"Hello, {name}!")

# ========================================
#                   Task4
# ========================================
full_name = input("Enter your full name: ")
first_name = full_name.split(" ")[0]
last_name = full_name.split(" ")[-1]        
print(first_name[0] + last_name[0])

# ========================================
#                   Task5
# ========================================
name = input("Enter your name: ")
while True:
    age = input("Enter your age: ")
    try:
        age = int(age)
        print(f"{name} is {age} years old.")
        break
    except ValueError:
        print("Invalid input")
        continue
