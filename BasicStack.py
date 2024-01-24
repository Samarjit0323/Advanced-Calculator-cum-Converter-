s=[]
while True:
    print("1.Push\n2.Pop\n3.Display")
    choice=str(input("Enter your choice::"))
    if choice=="1":
        m=int(input("Enter any number:"))
        s.append(m)
    elif choice=="2":
        if s==[]:
            print("Empty stack.")
        else:
            print("Deleted item is:",s.pop())
    elif choice=="3":
        if s==[]:
            print("Empty Stack.")
        else:
            l=len(s)
            for i in range(l-1,-1,-1):
                print(s[i])
    elif choice!=1 or choice!=2 or choice!=3:
        print("Wrong choice.")
    ch=input("DO WANT TO CONTINUE(y/n):")
    if ch=="y":
        continue
    elif ch=="n":
        break
print("Program ended.")
