# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y=map(int,input().split())
    if X>Y :
        print("NEW PHONE")
    elif X==Y :
        print("ANY")
    else :
        print("REPAIR")