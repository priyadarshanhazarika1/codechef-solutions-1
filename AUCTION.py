# cook your dish here
T=int(input())
for i in range(0,T):
    A,B,C=input().split()
    a=int(A)
    b=int(B)
    c=int(C)
    if(a>b and a>c):
        print("Alice")
    elif(b>a and b>c):
        print("Bob")
    else:
        print("Charlie")