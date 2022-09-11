# cook your dish here
T=int(input())
for i in range(0,T):
    N,M,K=map(int,input().split())
    e=M*K
    if e>=N :
        print("Yes")
    else :
        print("No")
        