# cook your dish here
T=int(input())
for i in range(0,T):
    X1,Y1,X2,Y2=input().split()
    x1=int(X1)
    y1=int(Y1)
    x2=int(X2)
    y2=int(Y2)
    style1=x1+y1
    style2=x2+y2
    if (style1<style2):
        print(style1)
    else:
        print(style2)