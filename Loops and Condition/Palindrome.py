# title : Palindrome
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I
n1 = input()
if int(n1)==int(n1[::-1]):
    print(int(n1[::-1]))
    print('YES')
else:
    print(int(n1[::-1]))
    print('NO')