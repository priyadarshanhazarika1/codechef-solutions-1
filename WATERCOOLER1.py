# cook your dish here
T=int(input())
for i in range(0,T):
    x,y,m=map(int,input().split())
    r=x*m 
    if r<y :
        print("YES")
    else :
        print("NO")