#To find the area,perimeter of 2D and area,volume of 3D objects
import math
def square(side):
    area=side*side
    perimeter=4*a
    resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
    return resultdict
def triangle(side1,side2,side3):
    perimeter=side1+side2+side3
    s=perimeter/2
    if (side1+side2)>side3 and (side1+side3)>side2 and (side3+side2)>side1:
        area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
        resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
        return resultdict
    else:
        return "Error: Invalid Triangle"
def rectangle(length,breadth):
    perimeter=2*(length+breadth)
    area=length*breadth
    resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
    return resultdict
def circle(radius):
    area=math.pi*radius*radius
    perimeter=2*math.pi*radius
    resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
    return resultdict
def parallelogram(side,base,height):
    area=base*height
    perimeter=2*(side+base)
    resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
    return resultdict
def rhombus(side,diag1,diag2):
    area=(1/2)*(diag1*diag2)
    perimeter=4*side
    resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
    return resultdict
def trapezium(shortbase,longbase,side3,side4,height):
    perimeter=shortbase+longbase+side3+side4
    area=(1/2)*(shortbase+longbase)*height
    resultdict={"Area(in sq. cm)":area,"Perimeter(in cm)":perimeter}
    return resultdict
def cuboid(length,breadth,height):
    volume=length*breadth*height
    tsa=2*((length*breadth)+(length*height)+(breadth*height))
    csa=2*(length+breadth)*h
    resultdict={"Total Surface Area(in sq. cm)":tsa,"Curved Surface Area(in sq. cm)":csa,"Volume (in cubic cm)":volume}
    return resultdict
def cube(side):
    volume=math.pow(side,3)
    tsa=6*math.pow(side,2)
    csa=4*math.pow(side,2)
    resultdict={"Total Surface Area(in sq. cm)":tsa,"Curved Surface Area(in sq. cm)":csa,"Volume (in cubic cm)":volume}
    return resultdict
def cylinder(radius,height):
    volume=math.pi*(radius**2)*height
    tsa=2*math.pi*radius*(radius+height)
    csa=2*math.pi*radius*height
    resultdict={"Total Surface Area(in sq. cm)":tsa,"Curved Surface Area(in sq. cm)":csa,"Volume (in cubic cm)":volume}
    return resultdict
def cone(base_radius,height):
    slant_height=math.sqrt(math.pow(height,2)+math.pow(base_radius,2))
    volume=(1/3)*math.pi*math.pow(base_radius,2)*height
    csa=math.pi*base_radius*slant_height
    tsa=(math.pi*base_radius*slant_height)+(math.pi*math.pow(base_radius,2))
    resultdict={"Slant height (in cm)":slant_height,"Total Surface Area(in sq. cm)":tsa,"Curved Surface Area(in sq. cm)":csa,"Volume (in cubic cm)":volume}
    return resultdict
def sphere(radius):
    volume=(4/3)*math.pi*math.pow(radius,3)
    surface_area=4*math.pi*math.pow(radius,2)
    resultdict={"Surface Area(in sq. cm)":surface_area,"Volume (in cubic cm)":volume}
    return resultdict
def hemisphere(radius):
    volume=(2/3)*math.pi*math.pow(radius,3)
    curved_surface_area=2*math.pi*math.pow(radius,2)
    total_surface_area=3*math.pi*math.pow(radius,2)
    resultdict={"Total Surface Area(in sq. cm)":total_surface_area,"Curved Surface Area(in sq. cm)":curved_surface_area,"Volume (in cubic cm)":volume}
    return resultdict
shapelist2D=["Circle","Triangle","Rectangle","Square","Parallelogram","Rhombus","Trapezium"]
shapelist3D=["Cube","Cuboid","Cylinder","Cone","Sphere","Hemisphere"]
Type=str(input("Enter the type of object(2D or 3D):"))
if Type=="2D":
    shape=str(input("Enter the required shape(capitalize first letter):"))
    if shape in shapelist2D:
        print("Now enter the dimensions in cm")
        if shape=="Square":
            a=float(input("Enter the side:"))
            print(square(a))
        elif shape=="Triangle":
            a=float(input("Enter first side:"))
            b=float(input("Enter second side:"))
            c=float(input("Enter third side:"))
            print(triangle(a,b,c))
        elif shape=="Rectangle":
            l=float(input("Enter the length:"))
            b=float(input("Enter the breadth:"))
            print(rectangle(l,b))
        elif shape=="Circle":
            r=float(input("Enter radius:"))
            print(circle(r))
        elif shape=="Parallelogram":
            a=float(input("Enter first side:"))
            b=float(input("Enter the second side or base:"))
            h=float(input('Enter heigth of perpendicular:'))
            print(parallelogram(a,b,h))
        elif shape=="Rhombus":
            d1=float(input("Enter the length of first diagonal:"))
            d2=float(input("Enter the length of second diagonal:"))
            a=float(input("Enter the side:"))
            print(rhombus(a,d1,d2))
        elif shape=="Trapezium":
            a=float(input("Enter the length of short base:"))
            b=float(input("Enter length of long base:"))
            c=float(input("Enter one of remaining two sides:"))
            d=float(input("Enter the last side:"))
            h=float(input("Enter the altitude:"))
            print(trapezium(a,b,c,d,h))
    else:
        print("Invalid Shape :(")
elif Type=="3D":
    obj=str(input("Enter the required object(capitalize first letter):"))
    if obj in shapelist3D:
        print("Now enter the values in cm")
        if obj=="Cuboid":
            l=float(input("Enter the length:"))
            b=float(input("Enter the breadth:"))
            h=float(input("Enter the heigth:"))
            print(cuboid(l,b,h))
        elif obj=="Cube":
            a=float(input("Enter length of edge:"))
            print(cube(a))
        elif obj=="Cylinder":
            r=float(input("Enter  base radius:"))
            h=float(input("Enter the heigth:"))
            print(cylinder(r,h))
        elif obj=="Cone":
            r=float(input("Enter  base radius:"))
            h=float(input("Enter the heigth:"))
            print(cone(r,h))
        elif obj=="Sphere":
            r=float(input("Enter radius:"))
            print(sphere(r))
        elif obj=="Hemisphere":
            r=float(input("Enter radius:"))
            print(hemisphere(r))
        else:
            print("Object not within range of program :(")
else:
    print("Figure type not within range of program :( You entered neither 2D or 3D!!! Restart.....")
            
            
        
        
            
            
            
            
        
