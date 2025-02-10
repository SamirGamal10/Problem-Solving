# Title : N Times
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/H
def Ntimes(number_case):
    for i in range(number_case):
        inputs=input().split()
        n1=int(inputs[0])
        n2=str(inputs[1])
        print(n1*f' {n2}')
number_case=int(input())
Ntimes(number_case)