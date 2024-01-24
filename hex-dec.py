char=["A","B","C","D","E","F"]
charnum=[10,11,12,13,14,15]
dec=0
n=str(input("Enter hexadecimal value:"))
lst=list(n)
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
        s=char.index(lst[a])
        k=charnum[s]
        m=k*z
        dec=dec+m
print("Equivalent decimal number:",dec)