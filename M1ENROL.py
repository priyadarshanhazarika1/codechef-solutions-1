# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    if(y>x):
        print(y-x)
    elif(y<=x):
        print(0)