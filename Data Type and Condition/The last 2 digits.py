# title : The last 2 digits
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Y
inputs = input().split()
n1 = int(inputs[0])
n2 = int(inputs[1])
n3 = int(inputs[2])
n4 = int(inputs[3])
N=n1*n2*n3*n4
if N%100==0:
    print('00')
elif len(str(N%100))==1:
    print(f'{0}{N%100}')
else:
    print(N%100)