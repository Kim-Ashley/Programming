# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    # TODO: Implement this function
    
    numbers = [num1, num3, num3]
    maximum = max(numbers)
    return maximum

#Taking 3 numbers as input from user
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))
#Printing maximum number among 3 numbers
print('The maximum number is:', built_in_functions_max(num1, num2, num3))

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    # TODO: Implement this function
    
    numbers = [num1, num2, num3] #list of numbers
    minimum = min(numbers)
    return minimum

#Taking 3 random numbers as input from user
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

#Printing minimum number among 3 numbers
print('The minimum number is: ', built_in_functions_min(num1, num2, num3))

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    # TODO: Implement this function
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."
    

#Taking a number as input from user
number = float(input('Enter a number: '))
#Printing whether the number is positive, negative or zero
print('The result is: ', check_number(number))

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    # TODO: Implement this function
    star = "*"
    for i in range(rows):
        print(star * (i + 1))
    pass  # Replace with your code
rows = int(input("Enter number of rows: "))
star_shape(rows)

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    # TODO: Implement this function
    count = 1
    while count <= limit:
        if count % 3 == 0:
            print("Multiple of 3")
        else:
            print(count)
        count += 1
    return limit

limit = int(input("Enter a positive integer: "))
print(count_multiples_of_3(limit))

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
    total = 0 
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

start = int(input('Enter the start of the range: '))
end = int(input('Enter the end of the range: '))
print('The sum of even numbers in the range is:', sum_of_even_numbers(start, end))