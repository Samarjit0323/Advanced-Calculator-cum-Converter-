num=str(input("Enter a binary number:"))
lst=list(num)
dec=0
for a in range(len(lst)):
    k=int(lst[a])
    y=1
    for x in range(len(lst)-1-a):
        y=y*2
    part=k*y
    dec=dec+part
print("Equivalent decimal number:",dec)
