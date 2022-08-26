# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=input().split()
    x=int(X)
    y=int(Y)
    if x>y:
        print("A")
    else:
        print("B")