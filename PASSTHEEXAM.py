# cook your dish here
T=int(input())
for i in range(0,T):
    A,B,C=map(int,input().split())
    s=A+B+C
    if s>=100 and A>=10 and B>=10 and C>=10 :
        print("PASS")
    else :
        print("FAIL")