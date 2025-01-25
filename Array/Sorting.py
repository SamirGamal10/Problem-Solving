# Title : Sorting
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/H
l = []
n = int(input())
inputs = input().split()
for i in range(n):
    a = int(inputs[i])
    l.append(a)
print(str(sorted(l)).replace("[", "").replace("]", "").replace(',',''))