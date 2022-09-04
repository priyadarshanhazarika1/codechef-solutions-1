# cook your dish here
T=int(input())
for i in range(0,T):
    X,Y,Z=input().split()
    x=int(X)
    y=int(Y)
    z=int(Z)
    rupees=(x*5)+(y*10)
    #print(m)
    cost=rupees//z
    print(cost)