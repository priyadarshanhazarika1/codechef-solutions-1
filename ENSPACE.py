# cook your dish here
T=int(input())
for i in range(0,T):
    N,X,Y=input().split()
    n=int(N)
    x=int(X)
    y=int(Y)
    if(x*1+y*2<=n):
        print("YES")
    else:
        print("NO")