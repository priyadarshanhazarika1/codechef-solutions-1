# cook your dish here
T=int(input())
for i in range(0,T):
    X,P,Q=input().split()
    x=int(X)
    p=int(P)
    q=int(Q)
    w=p-q
    f=x*w
    print(f)
    