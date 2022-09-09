# cook your dish here
T=int(input())
for i in range(0,T):
    N,M,X=map(int,input().split())
    cm=(2*N)+(2*M)
    print(cm*X)