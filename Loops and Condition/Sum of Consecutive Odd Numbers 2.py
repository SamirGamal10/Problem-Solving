# Title : Sum of Consecutive Odd Numbers
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S
number_case=int(input())
for index in range(number_case):
    inputs=input().split()
    n1=int(inputs[0])
    n2=int(inputs[1])
    l=[]
    if n1<n2:
        for i in range(n1+1,n2):
            if i%2==1 :
                l.append(i)
    else:
        for i in range(n2+1,n1):
            if i%2==1 :
                l.append(i)
    print(sum(l))