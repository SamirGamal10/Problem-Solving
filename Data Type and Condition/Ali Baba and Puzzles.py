# Title : Ali Baba and Puzzles
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/D
inputs=input().split()
n1=int(inputs[0])
n2=int(inputs[1])
n3=int(inputs[2])
r=int(inputs[3])
if n1+n2-n3==r or n1+n2*n3==r or n1-n2+n3==r or n1-n2*n3==r or n1*n2-n3==r or n1*n2+n3==r:
    print('YES')
else:
    print('NO')