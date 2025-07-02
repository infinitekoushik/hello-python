# Try-Except in Python (Error handling)

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Done handling errors.")
