# Title : Max and MIN
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/G
def MaxMin(number_case):
    l=[]
    inputs=list(map(int, input().split()))
    for i in range(number_case):
        a=inputs[i]
        l.append(a)
    print(min(l),max(l))
number_case=int(input())
MaxMin(number_case)