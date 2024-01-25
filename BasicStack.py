stack=[]
while True:
    print("1.Push\n2.Pop\n3.Display")
    choice=str(input("Enter your choice::"))
    if choice=="1":
        m=int(input("Enter any number:"))
        stack.append(m)
    elif choice=="2":
        if stack==[]:
            print("Empty stack.")
        else:
            print("Deleted item is:",stack.pop())
    elif choice=="3":
        if stack==[]:
            print("Empty Stack.")
        else:
            l=len(stack)
            for i in range(l-1,-1,-1):
                print(stack[i])
    elif choice!=1 or choice!=2 or choice!=3:
        print("Wrong choice.")
    ch=input("DO WANT TO CONTINUE(y/n):")
    if ch=="y":
        continue
    elif ch=="n":
        break
print("Program Terminated.")
