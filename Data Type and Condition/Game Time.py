# title : Game Time
# Link : https://codeforces.com/group/usP2We5vrA/contest/278273/problem/R
inputs=input().split()
a=int(inputs[0])
b=int(inputs[1])
if a==b:
    print('THE GAME LASTED 24 HOUR(S)')
elif a>b:
    print(f'THE GAME LASTED {b-(a-24)} HOUR(S)')
elif b>a:
    print(f'THE GAME LASTED {b-a} HOUR(S)')