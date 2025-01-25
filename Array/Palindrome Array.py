# Title : Palindrome Array
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G
l = []
n = int(input())
inputs = input().split()
for i in range(n):
    a = int(inputs[i])
    l.append(a)
if l==l[::-1]:
    print('YES')
else:
    print('NO')