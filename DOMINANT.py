# cook your dish here
T=int(input())
for i in range(0,T):
    a,b,c=map(int,input().split())
    if a+b<c or b+c<a or c+a<b :
        print("YES")
    else :
        print("NO")