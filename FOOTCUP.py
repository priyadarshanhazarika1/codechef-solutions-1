# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=map(int,input().split())
    if X>=1 and Y>=1 and X==Y:
        print("YES")
    else :
        print("NO")