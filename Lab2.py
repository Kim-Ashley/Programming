# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    
    #variable
    g = 9.8
    
    #Calculating height
    height1 = float(h0) - 0.5 * g * float(t)**2 

    #Printing the height
    

h0 = input("Enter initial height: ")
t = input("Enter time: ")

print("Height of the ball after " + str(t) + " seconds = " + str(height1))

calculate_height(h0, t) 



# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
   
   #variable
   speed = 20 
  
  #Calculate the distance 
   Distance = speed * float(t) 

   #Printing the distance
   print("The car will travel 20 m/s in " + str(t) + " seconds")

t = input("Enter time for car (in seconds): ")
calculate_car_distance(t)
