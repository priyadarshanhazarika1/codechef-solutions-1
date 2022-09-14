# cook your dish here
T=int(input())
for i in range(0,T):
    r1,r2,r3,r4=map(int,input().split())
    if r1==r2==r3==r4==0 :
        print("IN")
    else :
        print("OUT")