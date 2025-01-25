# Title : Sum Digits
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K
l=[]
n=int(input())
inputs=input()
for i in range(n):
    b=int(inputs[i])
    for g in str(b):
        l.append(int(g))
print(sum(l))