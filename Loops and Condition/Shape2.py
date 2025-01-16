# title : Shape2
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/S
n=int(input())
b=n-1
for index in range((n*2+1)):
    if index%2==1:
        a=index*'*'
        print('{}{}'.format(b*' ', a))
        b-=1