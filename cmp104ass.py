
#Program to solve Differnt Maths problelms
import math

def area_of_circle():
    """Function that defines an area of a circle"""
    print(" program to find area of a circle")
    a = float(input("Enter the value of a: "))
    b = a * a
    return b

print ("The result is ",area_of_circle())

#  Program to find Area of a Rectangle using Functions

def Area_of_a_Rectangle():
    print(" program to find area of a rectangle")
    l = float(input("Enter the Value of l: "))
    b = float(input("Enter the Value of b: "))
    a = l * b
    return a
print ("The result is ",Area_of_a_Rectangle())

def Area_of_a_triangle():
  print(" program to find area of a Triangle")  
  b = float(input("Enter the Value of b: "))
  h = float(input("Enter the Value of h: "))
  r = 1 / 2 * (b * h)
  return r
print ("The result is ",Area_of_a_triangle())

def Area_of_a_trapezoid():
    print("Calculate the area of a Trapezoid(Formula:1/2 x (b1 + b2)xh:)")\n
    b1 = float(input("Enter the Value of b1: "))
    b2= float(input("Enter the Value of b2: "))
    h= float(input("Enter the Value of h: "))
    r = 1 / 2 * (b1 + b2) * h
    return r
print ("The result is ",Area_of_a_trapezoid())
