# Title : Reversing
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/F
l = []
n = int(input())
inputs = input().split()
for i in range(n):
    a = int(inputs[i])
    l.append(a)
print(str(l[::-1]).replace("[", "").replace("]", "").replace(',',''))