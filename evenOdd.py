def check_even_odd(x):
    

    # Use if/else statement to check if the number is even or odd
    if x % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


# Get user input
num = int(input("Enter a whole number: "))

# Call the function to run the program
check_even_odd(num)