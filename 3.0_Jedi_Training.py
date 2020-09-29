# Sign your name: Geni W
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
username= input("Please enter your name: ")
print("Hello",username, end= '.')
print()
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base=int(input("Please enter the base of the triangle: "))
height=float(input("Please enter the height of the triangle: "))
area=base*height/2
print("The triangle\'s area is:" ,area,)
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius= int(input("Please enter the radius of the circle: "))
circum= 2*3.14*radius
print("The circle\'s circumference is:" ,circum,)
# 4. Ask a user for an integer and then print the square root.
integer= int(input("Please enter an integer: "))
sqrt= integer**0.5
print("The square root of %0.2f is %0.2f" %(integer ,sqrt))
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass=int(input("Please enter the mass: "))
accel=float(input("Please enter the acceleration: "))
force=mass*accel
print("The force is:" ,force,)
print("May the mass times acceleration be with you!")
print("Get it?")