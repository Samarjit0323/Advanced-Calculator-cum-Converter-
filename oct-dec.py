n=str(input("Enter an octal number:"))
lst=list(n)
dec=0
for a in range(len(lst)):
    k=int(lst[a])
    y=1
    for x in range(len(lst)-1-a):
        y=y*8
    part=k*y
    dec=dec+part
if dec>=33:
    print("Equivalent ASCII Character:",chr(dec))
print("Equivalent decimal number:",dec)
