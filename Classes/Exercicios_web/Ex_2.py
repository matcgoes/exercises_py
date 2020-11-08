#Source on: https://erlerobotics.gitbooks.io/erle-robotics-learning-python-gitbook-free/classes/exercisesclasses.html

#Ex1:
# Follow the steps:
# Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. 
# Make sure to set these appropriately in the body of the __init__()method.
# Create a variable named number_of_sides and set it equal to 3.
# Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
# Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
# Print out my_triangle.number_of_sides and print out my_triangle.check_angles().

class Triangle:
    """
    This class verifies wether a triangle is valid according to its angles (sum of 3 angles equals to 180 degrees).
    Moreover, there's a variable called "number_of_sides" which has '3' as set value.
    """
    def __init__(self,ang1,ang2,ang3):
        self.ang1 = ang1
        self.ang2 = ang2
        self.ang3 = ang3
    
    number_of_sides = 3
    
    def check_angles(self):
        return bool(self.ang1 + self.ang2 + self.ang3 == 180)
    
# my_triangle = Triangle(float(input("Angle 1: ")),float(input("Angle 2: ")), float(input("Angle 3: ")))

# print(my_triangle.number_of_sides)
# print(my_triangle.check_angles())

# Ex2:
# Define a class called Songs, it will show the lyrics of a song. Its __init__() method should have two arguments:
# self and lyrics. lyrics is a list. Inside your class create a method called sing_me_a_song that prints each element of 
# lyrics on his own line. Define a varible:

# happy_bday = Song(["May god bless you, ",
#                    "Have a sunshine on you,",
#                    "Happy Birthday to you !"])
# Call the sing_me_songmehod on this variable.

class Song:
    """
    Defined class which 'sings' an input song by user as a list format
    """

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for i in range(len(self.lyrics)):
            print(self.lyrics[i])

happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

# happy_bday.sing_me_a_song()

#Ex3:
# Define a class called Lunch.Its __init__() method should have two arguments: self and f menu.
# Where menu is a string. Add a method called menu_price.It will involve a ifstatement:
#     if "menu 1" print "Your choice:", menu, "Price 12.00", 
#     if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
#     To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().

class Lunch:
    """
    Returns a price based on menu choice.
    """
    def __init__(self,menu):
        self.menu = menu
    
    def menu_price(self):
        if self.menu == 'menu 1':
            print(f"Your choice: {self.menu}")
            print("Price: 12.00")
        elif self.menu == 'menu 2':
            print(f"Your choice: {self.menu}")
            print("Price: 13.40")
        else:
            print("Error in menu")
        
Paul = Lunch('menu 2')
Paul.menu_price()


# Ex4:
# Define a Point3D class that inherits from object Inside the Point3D class, 
# define an __init__() function that accepts self, x, y, and z, and assigns these numbers to the member variables 
# self.x,self.y,self.z. Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z). 
# This tells Python to represent this object in the following format: (x, y, z). 
# Outside the class definition, create a variable named my_point containing a 
# new instance of Point3D with x=1, y=2, and z=3. Finally, print my_point.

class Point3D:
    """
    Returns a Carthesian point formatted as (x,y,z)
    """

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)

print(my_point)