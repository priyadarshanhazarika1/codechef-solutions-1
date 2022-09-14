# cook your dish here
T=int(input())
for i in range(0,T):
    N,M,K=map(int,input().split())
    s=N+K
    if s<=M:
        print("Yes")
    else :
        print("No")