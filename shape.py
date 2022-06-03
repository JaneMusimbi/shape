import math

# Create the following python classes inside shapes.py

# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr
class Circle:
    def __init__(self,r):
     self.r = r
    def area_circle(self):
        A = math.pi *self.r**2
        return A
    def circumference(self):
        c = math.pi*2*self.r
        return c  

#         Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a  
class Square:
    def __init__(self,a):
        self.a=a
    def area_square(self):
        M=self.a**2
        return M    
def perimeter(self):
    V=4*self.a
    return V

# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l   
    def area_rectangle(self):
        p=self.w*self.l
        return p
def perimeter(self):
    L=2(self.l+self.w)
    return L

#  Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
class Sphere:
    def __init__(self,r):
        self.r=r
    def surface_area(self):
        N=4*math.pi*self.r**2
        return N

def volume(self):
    Q=4/3*math.pi*self.r**3
    return Q        

        

        













