import string
from itertools import *

casex = []
casey = []
points_c = 0

#entering points function
def points_enter():
    points_c = input("Enter number of points: ")
    if points_c.isdigit() == False or int(points_c) < 3:
        while points_c.isdigit() == False or int(points_c) < 3:
            print("Invalid number of points")
            points_c = input("Enter number of points: ")
    points_c = int(points_c)
    return  points_c

#enetering coordinates & preparing calculations
def coordinate_insert():
    points = list(string.ascii_lowercase)
    res = {}
    for i in range(points_c):
        x = input("Enter x coordinbate ")
        if x.isdigit() == False:
            while x.isdigit() == False:
                x = input("x coordinate was incorrect, retry input ")
        y = input("Enter y coordinate ")
        if y.isdigit() == False:
            while y.isdigit() == False:
                y = input("y coordinate was incorrect, retry input ")
        res[points[i]] = x,y
    casex = []
    casey = []
    for x,y in res.values():
        casex.append(float(x))
        casey.append(float(y))

    operate_case = []
    for i in range(points_c):
        k = [casex[i], casey[i]]
        operate_case.append(k)
    
    return res, casex, casey, operate_case

#Checking convexity
def CrossProduct(A):

    #Calculating vectors directions
    x1 = (A[1][0] - A[0][0])
    y1 = (A[1][1] - A[0][1])
    x2 = (A[2][0] - A[0][0])
    y2 = (A[2][1] - A[0][1])

    return (x1 * y2 - y1 * x2)

def isConvex(points):
    n = len(points)
    prev = 0
    curr = 0

    for i in range(n):
        temp = [points[i], points[(i + 1) % n], points[(i + 2) % n]]

        curr = CrossProduct(temp)

        if (curr != 0):
            if (curr * prev <  0):
                return False
            else:
                prev = curr
    return True

#All possible ways
def combinations(points):
    print("Checking all possible combinations...")
    general_case = []
    correct_one = None

    for i in permutations(points):
        general_case.append(i)
    
    for way in general_case:
        if isConvex(way) == True:
            correct_one = way
            print("Possible correct order was: ", correct_one)
            break
    return correct_one

def coordinates_printer(res):  
    #printing the dictionary
    for key, value in res.items():
        print("point",  key,"coordinates: ", value)

def square_calculation(casex, casey):
    #calculating A
    a = 0
    for i in range(points_c):
        a += (casex[(i+1) % points_c] + casex[i % points_c]) \
            * (casey[(i+1) % points_c] - casey[i % points_c])   
    a = a/2
    if a == 0:
        while a == 0:
            print("Square = 0, try another coordinates")
            res, casex, casey, operate_case = coordinate_insert()
            a = square_calculation(casex, casey)
    elif a < 0:
        print("Square < 0, program will operate with abs value")
        a = abs(a)

    return a

def other_calculations(casex, casey, a):
    print("A: ", round(a, 2))
    #calculating Sx
    Sx = 0
    for i in range(points_c):
        Sx += (casex[(i+1) % points_c] - casex[i % points_c]) \
            * (casey[(i+1) % points_c]**2 + casey[i % points_c] \
            * casey[(i+1) % points_c] + casey[i % points_c]**2)
    Sx = -Sx / 6
    print("Sx: ", round(Sx, 2))

    #calculating Sy
    Sy = 0
    for i in range(points_c):
        Sy += (casey[(i+1) % points_c] - casey[i % points_c]) \
            * (casex[(i+1) % points_c]**2 \
                + casex[i % points_c]*casey[(i+1) % points_c] \
                + casex[i % points_c]**2)
    Sy = Sy / 6
    print("Sy: ", round(Sy, 2))

    #calculating Ix
    Ix = 0
    for i in range(points_c):
        Ix += (casex[(i+1) % points_c] - casex[i % points_c]) \
            * (casey[(i+1) % points_c]**3 \
                + casey[(i+1) % points_c]**2 * casey[i % points_c] \
                + casey[(i+1) % points_c] * casey[i % points_c]**2 \
                + casey[i % points_c]**3)
    Ix = -Ix / 12
    print("Ix ", round(Ix, 2))

    #calculating Iy
    Iy = 0
    for i in range(points_c):
        Iy += (casey[(i+1) % points_c] - casey[i % points_c]) \
            * (casex[(i+1) % points_c]**3 \
                + casex[(i+1) % points_c]**2 * casex[i % points_c] \
                + casex[(i+1) % points_c] * casex[i % points_c]**2 \
                + casex[i % points_c]**3)
    Iy = Iy / 12
    print("Iy: ", round(Iy, 2))

    #calculating Ixy
    Ixy = 0
    for i in range(points_c):
        Ixy += (casey[(i+1) % points_c] - casey[i % points_c]) \
            * (casey[(i+1) % points_c] * (3*(casex[(i+1) % points_c]**2)\
                + 2*casex[(i+1) % points_c]*casex[i % points_c] \
                + casex[i % points_c]**2) \
                + casey[i % points_c] * ((3*(casex[i % points_c]**2)) \
                + 2*casex[(i+1) % points_c]*casex[i % points_c] \
                + casex[(i+1) % points_c]**2))
    Ixy = -Ixy/24
    print("Ixy: ", round(Ixy, 2))

    #calculating xt
    xt = Sy / a
    print("xt: ", round(xt, 2))

    #calculating yt
    yt = Sx / a
    print("yt: ", round(yt, 2))

    #calculating Itx
    Itx = Ix - yt**2 * a
    print("Itx: ", round(Itx, 2))

    #calculating Ity
    Ity = Iy - xt**2 * a
    print("Ity: ", round(Ity, 2))

    #calculating Itxy
    Itxy = Ixy + xt * yt *a
    print("Itxy: ", round(Itxy, 2))


#Main Body
input("Press Enter to start the program")
print("This program operates only with convex polygons")
points_c = points_enter()
res, casex, casey, operate_case = coordinate_insert()
a = square_calculation(casex, casey)


if isConvex(operate_case) != True:
    print("Order was incorrect, program will try to find correect order")
    check = combinations(operate_case)
    if check == None:
        while check == None:
            print("Invalid coordinates, there are no possible ways, retry input")
            res, casex, casey, operate_case = coordinate_insert()
            a = square_calculation(casex, casey)
            check = combinations(operate_case)
    casex = []
    casey = []
    res = {}
    print("Resetting coordinates...")
    points2 = list(string.ascii_lowercase)
    i = 0
    for each in check:
        casex.append(each[0])
        casey.append(each[1])
        res[points2[i]] = each[0], each[1]
        i += 1

coordinates_printer(res)
other_calculations(casex, casey, a)