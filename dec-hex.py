chardict={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
hexd=""
str1=""
num=int(input("Enter a decimal number:"))
while num>1:
    rem=int(num%16)
    if rem>9:
        rem=chardict.get(rem)
    num=num/16
    rem=str(rem)
    hexd=hexd+rem
lst=list(hexd)
for i in range(len(lst)):
    str1=str1+lst[-i-1]
print("Hexadecimal Equivalent:",str1)