# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
def calculate_height(h0, t):
    # TODO: Implement this function
    
    #variable
    g = 9.8
    
    #Calculating height
    height1 = float(h0) - 0.5 * g * float(t)**2

    #Returning the height
    return height1

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
   
    #variable
    speed = 20 
  
    #Calculate the distance 
    Distance = speed * float(t) 
    Final_distance = int(Distance)
    
    #Returning the distance
    return Final_distance



#Testing the function calculate_height
h0 = input("Enter initial height: ")
t = input("Enter time: ")
height1 = calculate_height(h0, t)
print("Height of the ball after " + str(t) + " seconds = " + str(height1) + " meters")

#Testing the function calculate_car_distance
t = input("Enter time for car (in seconds): ")
Final_distance = calculate_car_distance(t)
calculate_car_distance(t)
print("The car will travel " + str(Final_distance) + " meters in " + str(t) + " seconds")
