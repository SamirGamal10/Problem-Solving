# Title : Minimize Number
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
l = []
n = int(input())
inputs = input().split()
for i in range(n):
    a = int(inputs[i])
    l.append(a)
for g in l:
    if g%2==0:
        g/=2
        l.append(g)
    else:
        break
print(int((len(l)/n)-1))