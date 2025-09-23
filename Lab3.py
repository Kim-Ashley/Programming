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
    
r = float(input("Enter the value of r: "))
theta = float(input("Enter the value of theta (in degrees): "))

print(polar_to_cartesian(r, theta))


# Function 2(30): Convert Cartesian coordinates (x,y) to polar coordinates (r,θ).
# This function should take the Cartesian coordinates (x,y) as input and return the polar coordinates (r,θ).
def cartesian_to_polar(x, y):

    #Calculating r and theta
    r = math.sqrt(x**2 + y**2)
    
    #Calculating theta based on the quadrant
    theta = 0.0 
    if x == 0:
        if y > 0:
            theta = 90.0
        elif y < 0:
            theta = -90.0
        else:
            theta = 0.0
    
    if x < 0:
        theta_radians = math.atan(y / x) + math.pi
        theta = math.degrees(theta_radians)
    
    # If x > 0
    theta_radians = math.atan(y / x)
    theta = math.degrees(theta_radians)

    #Rounding the results into 5 decimal places 
    r = round(r, 5)
    theta = round(theta, 5)

    #Returning polar coordinates (r,θ)
    return (r, theta) 

x = float(input("Enter the value of x in radians: "))
y = float(input("Enter the value of y in radians: "))

print(cartesian_to_polar(x, y))

# Function 3 (40): Calculate the position of pendulum for (A, f, ϕ, t).
# This function should take (A, f, ϕ, t) as input and return the position value x.
def pendulum_position(A, f, phi, t):
    #Converting phi from degrees to radians
    phi_rad = math.radians(phi)

    #Angular frequency
    w = 2 * math.pi * f

    #Calculating the position x of the pendulum
    x = A * math.cos(w * t * phi_rad)

    #Rounding the position into 5 decimal places
    x = round(x, 5)

    #Returning pendulum position
    return x

#Putting the values (A, f, ϕ, t) as inputs 
A = float(input("Enter the value of A: "))
f = float(input("Enter the value of f: "))
phi = float(input("Enter the value of phi in degrees: "))
t = float(input("Enter the value of time in seconds: "))

print(f"The position of the pendulum is {pendulum_position(A, f, phi, t)}")