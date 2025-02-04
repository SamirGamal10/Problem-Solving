# Title : Good or Bad
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/H
number_case=int(input())
for i in range(number_case):
    a=str(input())
    if '010' in a or '101' in a:
        print('Good')
    else:
        print('Bad')