# Task 1: Create functions for each arithmetic operation

def add(num1, num2):
    total= num1 + num2
    print(f'{num1} + {num2} = {total}')

def sub(num1, num2):
    total= num1 - num2
    print(f'{num1} - {num2} = {total}')

def multi(num1, num2):
    total= num1 * num2
    print(f'{num1} * {num2} = {total}')

def div(num1, num2):
    total= num1 / num2
    print(f'{num1} / {num2} = {total}')

#Task 2: Implement user input to receive numbers and an operation choice.

print("lets do some math!")
number_1 = float(input("First lets start by picking a number: "))
number_2 = float(input("Ok now lets pick a second number: "))
print("Great! Now that we have out numbers picked out what mathmatical operation")
operation = input("We can add, subtract, multiply or divide. which would you like to do? ")
if operation == "add":
    add(number_1,number_2)
    print("Wow!! wasn't that fun!")
elif operation == "subtract":
    sub(number_1,number_2)
    print("Wow!! wasn't that fun!")
elif operation == "multiply":
    multi(number_1,number_2)
    print("Wow!! wasn't that fun!")
elif operation == "divide":
    div(number_1,number_2)
    print("Wow!! wasn't that fun!")
else:
    print("sorry that wasn't on of the option.")

# Task 3: Ensure your program can handle division by zero and other potential errors.

    # ran the appove code severl times for each function with arguments of 0 but was unable to come up with any error messages.
    # Not sure if this is a mistake in my code or how i formatted my function but the does not appear to be any errors to fix.