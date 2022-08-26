# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y,A=input().split()
    x=int(X)
    y=int(Y)
    a=int(A)
    if a>=x and a<y:
        print("YES")
    else:
        print("NO")