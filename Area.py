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
    obj=str(input("Enter the required object:"))
    if obj in shapelist3D:
        print("Now enter the values in cm")
        if obj=="Cuboid":
            l=float(input("Enter the length:"))
            b=float(input("Enter the breadth:"))
            h=float(input("Enter the heigth:"))
            vol=l*b*h
            tsa=2*(l*b+b*h+l*h)
            csa=2*(l+b)*h
            print("For a cuboid of dimensions",l,"cm X",b,"cm X",h,"cm;\nVolume =",vol,"cubic cm, TSA =",tsa,"sq.cm, CSA =",csa,"sq.cm.")
        elif obj=="Cube":
            a=float(input("Enter length of edge:"))
            vol=a**3
            tsa=6*(a**2)
            csa=4*(a**2)
            print("For a cube of edge",a,"cm;\nVolume=",vol,"cubic cm, TSA=",tsa,"sq.cm, CSA=",csa,"sq. cm.")
        elif obj=="Cylinder":
            r=float(input("Enter  base radius:"))
            h=float(input("Enter the heigth:"))
            vol=math.pi*r*r*h
            tsa=2*math.pi*r*(r+h)
            csa=2*math.pi*r*h
            print("For a cylinder of base radius",r,"cm, height",h,"cm;\nVolume=",vol,"cubic cm; TSA=",tsa,"sq.cm; CSA=",csa,"sq.cm")
        elif obj=="Cone":
            r=float(input("Enter  base radius:"))
            h=float(input("Enter the heigth:"))
            l=math.sqrt(r**2+h**2)
            vol=1/3*math.pi*r*r*h
            tsa=math.pi*r*(r+l)
            csa=math.pi*r*l
            print("The slant height of cone is",l,"cm.")
            print("For a cone of base radius",r,"cm, height",h,"cm, slant height=",l,"cm;\nVolume=",vol,"cubic cm; TSA=",tsa,"sq.cm; CSA=",csa,"sq.cm")
        elif obj=="Sphere":
            r=float(input("Enter radius:"))
            vol=4/3*math.pi*(r**3)
            sa=4*math.pi*r*r
            print("For a sphere of radius",r,"cm;\nVolume=",vol,"cubic cm; Surface Area=",sa,"sq.cm")
        elif obj=="Hemisphere":
            r=float(input("Enter radius:"))
            vol=2/3*math.pi*(r**3)
            csa=2*math.pi*r*r
            tsa=3*math.pi*r*r
            print("For a sphere of radius",r,"cm;\nVolume=",vol,"cubic cm; TSA=",tsa,"sq.cm; CSA=",csa,"sq.cm")
    else:
        print("Object not within range of program :(")
else:
    print("Figure type not within range of program :( You entered neither 2D or 3D!!! Restart.....")
            
            
        
        
            
            
            
            
        
