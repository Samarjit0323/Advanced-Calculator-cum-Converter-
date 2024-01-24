n=int(input("Enter decimal number:"))
lst=[]
str1=""
while n>=1:
    rem=n%2
    n=n//2
    k=str(rem)
    lst.append(k)
for a in range(len(lst)):
    b=lst[-a-1]
    str1+=b
print("Equivalent binary number:",str1)