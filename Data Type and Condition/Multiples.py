# title : Multiples
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/J
inputs = input().split()
A=int(inputs[0])
B=int(inputs[1])
if A%B==0 or B%A==0:
    print('Multiples')
else:
    print('No Multiples')