# cook your dish here
T=int(input())
for i in range(0,T):
    c,x,y=map(int,input().split())
    r=c-x
    print(r*y)