# Title : Positions in array
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/D
l = []
n = int(input())
inputs = input().split()
for i in range(n):
    a = int(inputs[i])
    l.append(a)
for idx, g in enumerate(l):
    if g <= 10:
        print(f'A[{idx}] = {g}')