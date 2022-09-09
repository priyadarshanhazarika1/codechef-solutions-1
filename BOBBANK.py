# cook your dish here
T=int(input())
for i in range(0,T):
    W,X,Y,Z=map(int,input().split())
    r=X-Y
    a=r*Z
    print(W+a)
