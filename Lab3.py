import math
# Function 1 (30): Convert the given polar coordinates (r,θ) to Cartesian coordinates (x,y). 
# This function should take the polar coordinates (r,θ) and return Cartesian coordinates (x,y).
def polar_to_cartesian(r, theta):
   
   #Converting degrees to radians
    theta_rad = math.radians(theta)

    #Calculating x and y coordianates
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)

    #Rounding the results into 5 decimal places
    x = round(x, 5)
    y = round(y, 5) 

    #Returning the coordinates
    return (x, y)
    
r = input("Enter the value of r: ")
theta = input("Enter the value of theta (in degrees): ")

print(polar_to_cartesian(r, theta))


# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):
    return (0, 0)

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    return 0