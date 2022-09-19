# cook your dish here
T=int(input())
for i in range(0,T):
    x,y,z=map(int,input().split())
    m=x+y
    if m<=z :
        print("2")
    elif x<=z :
        print("1")
    else :
        print("0")