# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    minimum=min(3*x,2*y)
    print(minimum)
    