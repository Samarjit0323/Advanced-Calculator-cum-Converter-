n=int(input("Enter decimal number:"))
lst=[]
str1=""
while n>1:
    rem=n%8
    n=n//8
    k=str(rem)
    lst.append(k)
lst.append("1")
for a in range(len(lst)):
    b=lst[-a-1]
    str1+=b
print("Equivalent octal number:",str1)