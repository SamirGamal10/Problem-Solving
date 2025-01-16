# title : Positive Numbers
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/I
count=0
for i in range(1,7):
    inputs=int(input())
    if inputs>0:
        count+=1
print(count)