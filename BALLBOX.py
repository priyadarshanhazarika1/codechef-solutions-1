# cook your dish here
T=int(input())
for i in range(0,T):
    N,K=map(int,input().split())
    a = K*(K+1)/2
    if (a<=N):
        print("YES")
    else :
        print("NO")
