# title : Easy Fibonacci
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y
n=int(input())
n1=0
n2=1
for i in range(n):
    print(n1,end=' ')
    n1, n2 = n2, n1 + n2