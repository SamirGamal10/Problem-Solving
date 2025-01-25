# Title : Replacement
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/C
l=[]
n=int(input())
inputs=input().split()
for i in range(n):
    a=int(inputs[i])
    l.append(a)
for g in l:
    if g>0:
        print(1,end=" ")
    elif g<0:
        print(2,end=" ")
    elif g==0:
        print(0,end=" ")