# Title : Lowest Number
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/E
l=[]
n=int(input())
inputs=input().split()
for i in range(n):
    a=int(inputs[i])
    l.append(a)
for g in l:
    if g==min(l):
        print(g,l.index(g)+1)
        break