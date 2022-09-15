# cook your dish here
T=int(input())
for i in range(0,T):
    w,x,y,z=map(int,input().split())
    l=y*z
    t=w+l
    if t>x :
        print("overFlow")
    elif t==x:
        print("filled")
    else :
        print("Unfilled")