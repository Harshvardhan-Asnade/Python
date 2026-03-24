try:
    a = int(input("Enter a number: "))
    result = 10 / a

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

else:
    print("Result is:", result)

finally:
    print("Program executed successfully (always runs)")