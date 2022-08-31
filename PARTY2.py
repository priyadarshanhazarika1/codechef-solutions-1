# cook your dish here
T=int(input())
for i in range(0,T):
    N,X,K=input().split()
    n=int(N)
    x=int(X)
    k=int(K)
    c=n*x
    if c<=k:
        print("YES")
    else:
        print("NO")