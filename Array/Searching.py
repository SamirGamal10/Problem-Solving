# Title : Searching
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/B
l=[]
n=int(input())
inputs=input().split()
for i in range(n):
    a=int(inputs[i])
    l.append(a)
b=int(input())
for g in l:
    if g==b:
        print(l.index(g))
        break
    elif b not in l:
        print(-1)
        break