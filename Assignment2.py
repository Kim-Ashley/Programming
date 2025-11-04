    # Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
   nums = [7, 3, 4, 5, 2, 4, 2]
   return sorted(set(nums))

nums = ""
print(remove_duplicates_and_sort(nums))

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result

arr = [1, 2, 3, 4]
print(cumulative_sum(arr))

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):

    return lst[::step]

lst = [1, 2, 3, 4, 5, 6]
print(slice_every_nth(lst, 2))

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    size = len(list1)
    index = 0
    total = 0
    while (index < size):
        total += list1[index] * list2[index]
        index += 1
    return total
 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(dot_product(list1, list2))

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    # Get row and column sizes
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Check if multiplication is possible
    if cols1 != rows2:
        return None  # or raise an error

    # Create an empty result matrix filled with zeros
    result = []
    for i in range(rows1):
        row = []
        for j in range(cols2):
            row.append(0)
        result.append(row)

    # Multiply the matrices
    for i in range(rows1):
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total += matrix1[i][k] * matrix2[k][j]
            result[i][j] = total

    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
print(matrix_multiplication(matrix1, matrix2))