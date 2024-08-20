

try:
    num = int(input("Enter a number: "))
    print("You entered: ", num)
    if num < 0:
        raise ValueError("Number should be positive")
except Exception as e:
    print("An error occurred: ", e)
finally:
    print("This code will always execute.")

