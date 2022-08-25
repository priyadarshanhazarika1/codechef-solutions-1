# cook your dish here
T=int(input())
for i in range(0,T):
    A,B,C=input().split()
    a=int(A)
    b=int(B)
    c=int(C)
    if((a+b)/2>=35 and (b+c)/2>=35 and (a+c)/2>=35):
        print("PASS")
    else:
        print("FAIL")