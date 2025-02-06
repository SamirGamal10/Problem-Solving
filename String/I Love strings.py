# Title : I Love strings
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/K
number_case=int(input())
for index in range(number_case):
    inputs=input().split()
    s=inputs[0]
    t=inputs[1]
    if len(s)<len(t):
        for i,j in zip(s,t):
            print(i+j,end='')
        print(t[len(s):len(t)],end='\n')
    elif len(s)>len(t):
        for i,j in zip(s,t):
            print(i+j,end='')
        print(s[len(t):len(s)],end='\n')
    else:
        for i,j in zip(s,t):
            print(i+j,end='')
        print(end='\n')