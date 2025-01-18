def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

print("Choose your operation-\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

# Prompt user to select an operation
select = int(input("Select operation (1/2/3/4): "))

# Input numbers
a = int(input("First number: "))
b = int(input("Second number: "))

# Perform the operation based on user input
if select == 1:
    print(f"Result: {add(a, b)}")
elif select == 2:
    print(f"Result: {sub(a, b)}")
elif select == 3:
    print(f"Result: {mul(a, b)}")
elif select == 4:
    if b != 0:  # Prevent division by zero
        print(f"Result: {div(a, b)}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid selection. Please choose a valid operation.")
