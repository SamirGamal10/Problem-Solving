# title : Dividing X by Y
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/K
n1=int(input())
for i in range(1,n1+1):
    inputs=input().split()
    x=int(inputs[0])
    y=int(inputs[1])
    if y==0:
        print('Impossible')
    else:
        print(round((x/y),1))