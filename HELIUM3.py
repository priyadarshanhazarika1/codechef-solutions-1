# cook your dish here
T=int(input())
for i in range(0,T):
    a,b,x,y=map(int,input().split())
    p=a*b
    m=x*y
    if m>=p :
        print("Yes")
    else :
        print("No")