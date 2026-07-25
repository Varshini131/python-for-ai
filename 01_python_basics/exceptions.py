try:
    number = int(input("Enter a number: "))
    print(100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid input.")

finally:
    print("Program Finished.")