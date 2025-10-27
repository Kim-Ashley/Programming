
# Function 1: Rotate the Array
# This function creates an array of a specified size, fills it with numbers starting from `starting_integer` and increasing by 3,
# then rotates elements at even indices 2 positions to the left.
def rotate_the_array(array_size, starting_integer):
   
   #Initialize array with size array_size
   arr = [0]*array_size

   #Fill up array with numbers starting from starting_integer and increasing by 3
   for i in range(array_size):
      arr[i] = starting_integer + 3* (array_size - 1 - i)

   #Rotate elements at even indicies 2 positions to the left
   for i in range(0, array_size - 2, 2): #range(start, stop, step)
      temp = arr[i]
      arr[i] = arr[i + 2]
      arr[i + 2] = temp

   return arr


array_size = int(input('Enter the size of array: '))
starting_interger = int(input('Enter a starting number: '))
print(rotate_the_array(array_size, starting_interger))













