# Title : Palindrome
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/I
l = []
A=str(input())
for i in list(A):
    l.append(i)
if l==l[::-1]:
    print('YES')
else:
    print('NO')