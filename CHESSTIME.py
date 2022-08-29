# cook your dish here
T=int(input())
for i in range(0,T):
    N=int(input())
    #1 hour= 60minutes
    total_mins=N*60
    no_games=int(total_mins/20)
    print(no_games)