# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=map(int,input().split())
    e=Y*30
    if X>=e :
        print("YES")
    else :
        print("NO")