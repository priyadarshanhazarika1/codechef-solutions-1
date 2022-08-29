# cook your dish here
T=int(input())
for i in range(0,T):
    A,B=input().split()
    a=int(A)
    b=int(B)
    if ((a+b)%2==0):
        print("YES")
    else:
        print("NO")