# title : Hard Compare
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Z
import math
inputs = input().split()
n1 = int(inputs[0])
n2 = int(inputs[1])
n3 = int(inputs[2])
n4 = int(inputs[3])
if n2*math.log(n1)>n4*math.log(n3):
    print('YES')
else:
    print('NO')