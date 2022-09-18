# cook your dish here
T=int(input())
for i in range(0,T):
    n,x=map(int,input().split())
    s=3*x
    print(int(n/s))