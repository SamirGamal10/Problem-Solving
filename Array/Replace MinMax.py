# Title : Replace MinMax
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M
l = []
n = int(input())
inputs = input().split()
for i in range(n):
    a = int(inputs[i])
    l.append(a)
min_index = l.index(min(l))
max_index = l.index(max(l))
l[min_index], l[max_index] = l[max_index], l[min_index]
print(str(l).replace("[", "").replace("]", "").replace(',',''))