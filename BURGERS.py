# cook your dish here
T=int(input())
for i in range(0,T):
    A,B=input().split()
    a=int(A)
    b=int(B)
    #burger=a+b
    m=[a,b]
    if(a-b==0):
        print(a)
    else:
        print(min(m))