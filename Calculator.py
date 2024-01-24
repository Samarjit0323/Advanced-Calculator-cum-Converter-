#Scientific Calculator
print("\t\t\t WELCOME TO PYTHON CALCULATOR\n\n")
print("Hello User!! . How may I help you?\n\n")
print("Please enter the keywords for performing respective operations in this calculator(Operation Keyword):")
print("Addition(+), Substraction(-), Multiply(*), Division(/), Exponents(^), Sine(sin), Cosine(cos), Tangent(tan), Exponential(expo), Factorial(fact)")
def add():
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print ("The result of this operation is",num1+num2,".")
def substract():
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print ("The result of this operation is",num1-num2,".")
def multiply():
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print ("The result of this operation is",num1*num2,".")
def divide():
    num1=float(input("Enter the dividend:"))
    num2=float(input("Enter the divisor:"))
    print("The quotient of this operation is",num1/num2,".")
    print("The remainder of this operation is",num1%num2,".")
import math
while True:
    print()
    op=input("Enter the type of operation you want to perform:")
    if op=="+":
        add()
    elif op=="-":
        substract()
    elif op=="*":
        multiply()
    elif op=="/":
        divide()
    elif op=="^":
        base=float(input("Enter the base number:"))
        power=float(input("Enter the power to be raised:"))
        print("The result of this operation is",math.pow(base,power),".")
    elif op=="fact":
        print("Please enter a POSITIVE INTEGER.")
        n=int(input("Enter the required number:"))
        print(n,"! =",math.factorial(n))
    elif op=="sin":
        choice1=input("Is the input in radians?(y/n):")
        if choice1=="n":
            deg=float(input("Enter the angle in degrees:"))
            rad=math.radians(deg)
            print("sin(",rad,")=",math.sin(rad))
        elif choice1=="y":
            rad=float(input("Enter the angle in radians:"))
            print("sin(",rad,")=",math.sin(rad))
    elif op=="cos":
        choice1=input("Is the input in radians?(y/n):")
        if choice1=="n":
            deg=float(input("Enter the angle in degrees:"))
            rad=math.radians(deg)
            print("cos(",rad,")=",math.cos(rad))
        elif choice1=="y":
            rad=float(input("Enter the angle in radians:"))
            print("cos(",rad,")=",math.cos(rad))
    elif op=="expo":
        x1=float(input("Enter the value to which e is to be raised:"))
        print("The result of exponential operation is", math.exp(x1))
    elif op=="tan":
        choice1=input("Is the input in radians?(y/n):")
        if choice1=="n":
            deg=float(input("Enter the angle in degrees:"))
            rad=math.radians(deg)
            print("tan(",rad,")=",math.tan(rad))
        elif choice1=="y":
            rad=float(input("Enter the angle in radians:"))
            print("tan(",rad,")=",math.tan(rad))
    elif op!="+" or op!="-" or op!="*" or op!="/" or op!="^" or op!="sin" or op!="cos" or op!="tan":
        print("Operation out of Calculator Operation Range. We'll soon include it ;)")
    choice=input("Do want to perform more operations?(y/n)")
    if choice=="y":
        continue
    else:
        break
        
print()
print("Thank you for using me. My upgradation is under process :-)")
    


