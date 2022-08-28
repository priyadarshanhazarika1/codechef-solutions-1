# cook your dish here
N=int(input())
for i in range(0,N):
    A,B,C=input().split()
    a=int(A)
    b=int(B)
    c=int(C)
    if(a>b and a<c):
        print(a)
    elif(a<b and a>c):
        print(a)
    elif(b>a and b<c):
        print(b)
    elif(b<a and b>c):
        print(b)
    else:
        print(c)