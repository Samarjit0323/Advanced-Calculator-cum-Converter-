#Convert hexadecimal value to a decimal one

dec=0
num=str(input("Enter hexadecimal value:"))
lst=list(num)
for a in range(len(lst)):
    if lst[a].isalpha()==False:
        y=1
        for x in range(len(lst)-1-a):
            y=y*16
        x=(int(lst[a]))*y
        dec=dec+x
    else:
        z=1
        for i in range(len(lst)-1-a):
            z=z*16
        s=chardict.get(lst[a])
        m=s*z
        dec=dec+m
print("Equivalent decimal number:",dec)