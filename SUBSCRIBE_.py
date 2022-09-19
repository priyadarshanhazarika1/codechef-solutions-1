# cook your dish here
T=int(input())
for i in range(0,T):
    n,x=map(int,input().split())
    a=n%6
    b=n//6
    if a==0 :
        print(b*x)
    else :
        print((b+1)*x)