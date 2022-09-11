# cook your dish here
T=int(input())
for i in range(0,T):
    A,B,C,D=map(int,input().split())
    f=A-C
    s=B-D
    if f<s :
        print("First")
    elif f==s :
        print("Any")
    else :
        print("Second")