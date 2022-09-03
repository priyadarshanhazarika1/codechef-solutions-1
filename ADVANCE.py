# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    d=x+201
    if(y in range(x,d)):
        print("YES")
    else:
        print("NO")