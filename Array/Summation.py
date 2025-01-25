# Title : Summation
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/A
l=[]
n=int(input())
inputs=input().split()
for i in range(n):
    a=int(inputs[i])
    l.append(a)
if sum(l)<0:
    print(sum(l)*-1)
else:
    print(sum(l))