# title : Six Odd Numbers
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/H
n=int(input())
for index in range(n,n+12):
    if index%2==1:
        print(index)