# Title : Digits
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q
l=[]
number_case=int(input())
for index in range(number_case):
    n=int(input())
    for i in str(n):
        l.append(i)
    print(str(l[::-1]).replace('[','').replace(']','').replace(',','').replace("'",''))
    l.clear()