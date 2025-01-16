# title : Even Square
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/F
n=int(input())
if n <2:
        print(-1)
for index in range(2,n+1):
    if index%2==0:
        print(f'{index}^2 = {index**2}')