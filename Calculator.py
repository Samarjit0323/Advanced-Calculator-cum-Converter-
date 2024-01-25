#Basic Calculator without module
print("WELCOME TO BASIC PYTHON CALCULATOR\n")
print("Hello User!! . How may I help you?\n")
print("Please enter the keywords for performing respective operations in this calculator(Operation Keyword):")
print("Addition(+), Substraction(-), Multiply(*),\nDivision(/), Exponents(^)(**integral power), Factorial(fact)")
def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    resultdict={"Quotient":a//b,"Remainder":a%b,"Actual Division":a/b}
    return resultdict
def power_raised(a,b):
    for i in range(b-1):
        a=a*a
    return a
def factorial(num):
    val=1
    for a in range(1,num+1):
        val=val*a
    return val
while True:
    print()
    op=input("Enter the type of operation you want to perform:")
    if op=="+":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print ("The result of this operation is",add(num1,num2))
    elif op=="-":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print ("The result of this operation is",substract(num1,num2))
    elif op=="*":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print ("The result of this operation is",multiply(num1,num2))
    elif op=="/":
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print ("The result of this operation is",divide(num1,num2))
    elif op=="^":
        base=float(input("Enter the base number:"))
        power=int(input("Enter the power to be raised:"))
        print(base,"raised to the power",power,"is",power_raised(base,power))
    elif op=="fact":
        print("Please enter a POSITIVE INTEGER.")
        n=int(input("Enter the required number:"))
        print(n,"! =",factorial(n))
    
    elif op!="+" or op!="-" or op!="*" or op!="/" or op!="^":
        print("Operation out of Calculator Operation Range. We'll soon include it ;)")
    choice=input("Do want to perform more operations?(y/n)")
    if choice=="y":
        continue
    else:
        break
print("\nThank you for using me.\nMy upgradation is under process :-)")
    


