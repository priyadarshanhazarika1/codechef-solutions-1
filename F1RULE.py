# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=map(int,input().split())
    s=107*X/100
    if Y<=s:
        print("YES")
    else :
        print("NO")