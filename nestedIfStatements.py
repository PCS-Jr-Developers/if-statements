# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is positive
if number > 0:
    print("The number is positive.")
    
    # Check if the positive number is even or odd
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not positive.")
