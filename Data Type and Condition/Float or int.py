# title : Float or int
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/U
inputs = input().split('.')
n1 = int(inputs[0])
n2=int(inputs[1])
if n2==0:
    print(f'int {n1}')
else:
    print(f'float {n1} 0.{n2}')