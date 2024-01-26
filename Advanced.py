import math
def factorial(n):
    final=1
    for i in range(1,n+1):
        final=final*i
    return final
def combination(n,r):
    #for n!
    n_top=factorial(n)
    n_r=factorial(n-r)
    r_bot=factorial(r)
    comb=n_top/(n_r*r_bot)
    return comb
def permutation(n,r):
    n_top=factorial(n)
    n_r=factorial(n-r)
    perm=n_top/n_r
    return perm
ch=str(input("Enter choice:"))
if ch=="sin":
    rad=float(input("Enter values in radians:"))
    print(math.sin(rad))
elif ch=="cos":
    rad=float(input("Enter values in radians:"))
    print(math.cos(rad))
elif ch=="tan":
    rad=float(input("Enter values in radians:"))
    print(math.tan(rad))
elif ch=="combination":
    print("For nCr:")
    n=int(input("Enter value of n:"))
    r=int(input("Enter value of r:"))
    print(n,"C",r,"=",combination(n,r))
elif ch=="permutation":
    print("For nPr:")
    n=int(input("Enter value of n:"))
    r=int(input("Enter value of r:"))
    print(n,"P",r,"=",permutation(n,r))