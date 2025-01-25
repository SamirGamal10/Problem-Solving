# Title : Lucky Array
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/J
l=[]
n=int(input())
inputs=input().split()
for i in range(n):
    a=int(inputs[i])
    l.append(a)
if (l.count(min(l)))%2==1:
    print('Lucky')
else:
    print('Unlucky')