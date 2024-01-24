char=["A","B","C","D","E","F"]
charnum=[10,11,12,13,14,15]
hexd=""
str1=""
n=int(input("Enter a decimal number:"))
while n>1:
    rem=int(n%16)
    if rem>9:
        k=charnum.index(rem)
        rem=char[k]
    n=n/16
    rem=str(rem)
    hexd=hexd+rem
lst=list(hexd)
for i in range(len(lst)):
    str1=str1+lst[-i-1]
print(str1)