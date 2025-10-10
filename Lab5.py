# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = "" # to store the pattern
    count = 0
    while count < n:
        if count == 0 or count == n - 1: # first or last row
            print ("*" * n)
        else:           # middle rows
            print("*" + " " * (n-2) + "*")
        count += 1 # increment count
    return result

#input and printing the pattern
n = int(input('Enter number of rows: '))
hollow_square(n)

# 1
# 12
# 123
# 1234

def number_pattern(n):
    result = "" 
    i = 1
    while i <= n:
        j = 1               # start from 1
        while j <= i:
            result += str(j)
            j += 1
        result += "\n" # new line
        i += 1  
    return result

#input and printing the pattern
n = int(input('Enter number of rows: '))   
print(number_pattern(n))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0                   # to store the sum
    i = 1                       # start from 1
    while i <= n:               # loop from 1 to n
        total += i              # add i to total
        i += 1                  # increment i
    return total

#input and printing the sum
n = int(input('Enter a number: '))
print(sum_of_natural_numbers(n))

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = "" # to store the pattern
    i = 1
    while i <= n:
        # spaces
        j = 1
        while j <= n - i:
            result += " "
            j += 1

        # stars
        k = 1
        while k <= 2 * i - 1:
            result += "*"
            k += 1

        result += "\n" # new line
        i += 1
    return result

#input and printing the pattern
n = int(input('Enter number of rows: '))
print(centered_star_pyramid(n))