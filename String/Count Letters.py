# Title : Count Letters
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/J
n1=str(input())
for index in sorted(set(n1)):
    print(f'{index} : {n1.count(index)}')