# cook your dish here
T=int(input())
for i in range(0,T):
    N,K=input().split()
    n=int(N)
    k=int(K)
    if(k>n):
        print("YES")
    else:
        print("NO")