a=int(input())
b=int(input())
c=int(input())
d=b**2-4*a*c
print("d =",d)
if d<0:
    print("��� �������")
if d==0:
    x=(-b+d**0.5)/2*a
    print(x)
if d>0:
    x1=(-b+d**0.5)/2*a
    print("x1 =",x1)
    x2=(b+d**0.5)/2*a
    print("x2 =",x2)
    
    

