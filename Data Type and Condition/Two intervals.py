# title : Two intervals
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/X
inputs = input().split()
l1 = int(inputs[0])
r1 = int(inputs[1])
l2 = int(inputs[2])
r2 = int(inputs[3])
if l1>l2:
    a=l1
else:
    a=l2
if r1>r2:
    b=r2
else:
    b=r1
if a>b:
    print('-1')
else:
    print(a,b)