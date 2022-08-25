# cook your dish here
T=int(input())
for i in range(0,T):
    A,B,C=input().split()
    #A=int(input())
    #B=int(input())
    #C=int(input())
    a=int(A)
    b=int(B)
    c=int(C)
    if ((a+b)/2>c):
       print("YES")
    else:
        print("NO")
