# cook your dish here
T=int(input())
for i in range(0,T):
    X,H=input().split()
    x=int(X)
    h=int(H)
    if x>=h:
        print("YES")
    else:
        print("NO")