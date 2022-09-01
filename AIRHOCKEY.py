# cook your dish here
T=int(input())
for i in range(0,T):
    A,B=input().split()
    a=int(A)
    b=int(B)
    alice=7-a
    bob=7-b
    if alice<=bob:
        print(alice)
    else:
        print(bob)