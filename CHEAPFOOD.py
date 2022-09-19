# cook your dish here
T=int(input())
for i in range(0,T):
    X=int(input())
    p=(X/10)
    d=X-100
    a=X-p
    b=X-d
    if p>b :
        print(int(p))
    else :
        print(b)