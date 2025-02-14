# Title : Square or rectangle
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/329103/problem/A
number_case=int(input())
for i in range(number_case):
    a, b = map(int, input().split())
    if a==b:
        print('Square')
    else:
        print('Rectangle')