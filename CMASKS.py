# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=map(int,input().split())
    d=X*100
    c=Y*10
    if d<c :
        print("Disposable")
    elif d==c :
        print("Cloth")
    elif d>c :
        print("Cloth")