def calc():
    print("Hello this Calculator is limited to what you can calculate")
    print("Enter an option below to calculate: 1-Area of a Square, 2-Area of a Rectangle,3-Area of a Triangle,4-Area of a Trapezoid, 5-Area of a Circle")
    print("6-Area of a Circumfrence, 7-Area of a cube, 8-Area of a Cylinder, 9-volume of a cylinder,10-Acceleration formula, 11-Density formula")
    print("12- Formula for pressure, 13- formula for kinetic Energy, 14-forumla for Voltage")
    x = int(input("Please Choose from the above options: "))
    if x == 1:
        print("Calculate the area of a Square (Formula :a x a:)")
        a = float(input("Enter the Value of a: "))
        b = a * a
        print("Hello the result is ",b)
    if x == 2:
        print("Calculate the area of a Rectangle (Formula :l x b:)")
        l = float(input("Enter the Value of l: "))
        b = float(input("Enter the Value of b: "))
        r = l * b
        print("Hello the result is ",r)
    if x == 3:
        print("Calculate the area of a Triangle (Formula :1/2 x b x h:)")
        b = float(input("Enter the Value of b: "))
        h = float(input("Enter the Value of h: "))
        r = 1 / 2 * (b * h)
        print("Hello the result is ",r)
    if x == 4:
        print("Calculate the area of a Trapezoid (Formula:1/2 x (b1 + b2)xh:)")
        b1 = float(input("Enter the Value of b1: "))
        b2 = float(input("Enter the Value of b2: "))
        h = float(input("Enter the Value of h: ")) 
        r = 1 / 2 * (b1 + b2) * h
        print("Hello the result is ",r)
    if x == 5:
        print("Calculate the area of a Cicle (Formula :PIxrxr:)")
        rd = float(input("Enter the Value of r: "))
        pi = 22/7
        s = rd * rd
        r = pi * s
        print("Hello the result is ",r)
    if x == 6:
        print("Calculate Surcface area of a Circumfrence (Formula :2xPIxr:)")
        rd = float(input("Enter the Value of r: "))
        pi = 22/7
        r = 2 * pi * rd
        print("Hello the result is ",r)
    if x == 7:
        print("Calculate the Surcface area of a Cube (Formula :6xaxa:)")
        a = float(input("Enter the Value of a: "))
        s = a * a 
        r = 6 * s
        print("Hello the result is ",r)
    if x == 8:
        print("Calculate curved surface area of a cylinder (Formula :2PIxrx(r+h):)")
        rd = float(input("Enter the Value of r: "))
        h = float(input("Enter the Value of h: "))
        pi = 22/7
        r = 2 * pi * rd * ( rd + h)
        print("Hello the result is ",r)
    if x == 9:
        print("Calculate the Volume of a Cyinder(Formula :PIx(rxr)*h:)")
        rd = float(input("Enter the Value of r: "))
        h = float(input("Enter the Value of h: "))
        pi = 22/7
        s = rd * rd
        r = pi * s * h
        print("Hello the result is ",r)
    if x == 10:
        print("Calculate the  Acceleration Formula(Formula :V-U/t:)")
        v = float(input("Enter the Value of v: "))
        u = float(input("Enter the Value of u: "))
        t = float(input("Enter the Value of t: "))
        r = (v - u) / t
        print("Hello the result is ",r)
    if x == 11:
        print("Calculate the Density Formula(Formula :M/V:)")
        m = float(input("Enter the Value of m: "))
        v = float(input("Enter the Value of v: "))
        r = m / v
        print("Hello the result is ",r)
    if x == 12:
        print("Calculate the Volume of a Cyinder(Formula :F/A:)")
        f = float(input("Enter the Value of f: "))
        a = float(input("Enter the Value of a: "))
        r = f / a
        print("Hello the result is ",r)
    if x == 13:
        print("Calculate the formula for kinetic Energy(Formula :1/2M(vxv):)")
        m = float(input("Enter the Value of m: "))
        v = float(input("Enter the Value of v: "))
        s = v * v 
        r = 1/2 * m * s
        print("Hello the result is ",r)
    elif x == 14:
        print("Calculate the formula for voltage(Formula :IR:)")
        i = float(input("Enter the Value of i: "))
        r = float(input("Enter the Value of r: "))
        ro = i * r
        print("Hello the result is ",ro)
    print("Thanks for Using the calculator")
    a = input("Enter r to restart the Calculator ")
    if a == r:
        return x
    else:
        b = input("Enter q to quit the calculator")

calc()
