# cook your dish here
T=int(input())
for i in range(0,T):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    
    if a<=c and b<=d :
        print("POSSIBLE")
    else :
        print("IMPOSSIBLE")