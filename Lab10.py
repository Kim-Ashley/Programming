import numpy as np
import matplotlib.pyplot as plt

# Function 1: Curve Plotting
def plot_curve(x_values, y_values):
  
    #Create a line chart
    plt.plot(x_values, y_values, marker = 'o', linestyle = '-')

    #Customize chart
    plt.title("Curve Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.grid(True)

    #Display chart
    graph = plt.show()
    
    return graph 

#Print curve plot
print(plot_curve([1, 2, 3, 4, 5],[5, 10, 15, 20, 25]))

# Function 2: Hertzsprung-Russell Diagram
def plot_hr_diagram(temperature, luminosity):
    
    #Create scatter plot
    plt.scatter(temperature, luminosity, c = temperature, cmap = 'plasma', edgecolors = 'k')

    #Labelling axis
    plt.title("Hertzsprung-Russel Diagram")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Luminosity (L)")

    #Decreasing x axis
    plt.gca().invert_xaxis()
    
    #Adding color bar
    plt.colorbar(label = "Temperature (K)")

    #Display diagram
    HR_diagram = plt.show()

    return HR_diagram

#Print Hertzsprung-Russel Diagram
print(plot_hr_diagram([11000, 9000, 7000, 5000, 3000], [1000, 100, 10, 1, 0]))

# Function 3: Heat Map and Density Plot
def plot_density(data, color_map='gray'):
   
    #Data x and y
    x = data[:,0]
    y = data[:,1]

    #Create 2D histogram
    plt.hist2d(x, y, bins = 50, cmap = color_map, density = True)

    #Labeling axis and title
    plt.title("Density Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    #Adding color bar
    plt.colorbar(label = "Density")

    #Display 2D Histogram
    density = plt.show()


    return density

#Printing density plot
data = np.random.rand(1000,2) 
print(plot_density(data, color_map='gray'))

# Example usage:
if __name__ == "__main__":
    # Example for plot_curve
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plot_curve(x, y)
    
    # Example for plot_hr_diagram
    temp = np.array([3000, 5000, 7000, 9000, 11000])
    lum = np.array([0.1, 1, 10, 100, 1000])
    plot_hr_diagram(temp, lum)
    
    # Example for plot_density
    np.random.seed(0)
    data = np.random.randn(1000, 2)  # Generating random 2D data
    plot_density(data, 'hot')
