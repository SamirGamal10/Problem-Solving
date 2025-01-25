# Title : Fibonacci
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/O
n=int(input())
l=[]
n1=0
n2=1
for i in range(n):
    l.append(n1)
    n1, n2 = n2, n1 + n2
print(l[-1])