import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):
    
    #Write to  a new file
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + "\n")
    
    #Read back
    with open(filename, 'r') as file:
        values = [int(line.strip()) for line in file]

    return values

#Printing txt file contents
print(write_and_read_txt("numbers.txt", [5, 10, 15, 20]))

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):

    #Creating csv file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)  #writing each inner list in 'data as one row in the CSV

    #Read from csv file
    read_data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #Converting current value from string to integer
            read_data.append([int(value) for value in row])

    return read_data

#Printing data from csv file
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(write_and_read_csv("data.csv", data))

# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    
    with open(filename, 'r') as file:
        line = file.readline().strip()  #read the entire line
        values = line.split()           #split by spaces
        values = [int(v) for v in values]   #convert each string value to integer
    return np.array(values)

print(read_array_from_file(r"c:\Users\kimas\OneDrive\Documents\Programming\Assignment 3\array.txt.txt"))

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):

    #Plotting lists of numbers as simple line graph
    plt.plot(numbers, marker = 'o', linestyle = '-')
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Line Plot of Numbers")
    plt.grid(True)
    line_graph = plt.show()
    return line_graph

#Print line graph
numbers = [1,2,3,4,5,6,7]
print(plot_data(numbers))

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data):
    
    #Plotting a density plot using 2D histogram
    plt.hist2d(test_data[:,0], test_data[:,1], bins = 50, cmap = 'gray', density = True)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.title("Density Plot")
    plt.grid(True)
    density = plt.show()
    return density

#Print 2D histogram
test_data = np.random.rand(2000,2)
print(density_plot(data))