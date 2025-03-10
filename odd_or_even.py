def check_number():
    number = int(input("Add number to check if it is even or odd: "))
    print(number, " is an even number." if number % 2 == 0 else " is an odd number.")
    
check_number()