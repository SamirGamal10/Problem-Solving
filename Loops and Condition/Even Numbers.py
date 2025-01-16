# title : Even Numbers
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/B
n=int(input())
if n <2:
        print(-1)
for index in range(2,n+1):
    if index%2==0:
        print(index)