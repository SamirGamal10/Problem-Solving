# Title : Sequence of Numbers and Sum
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/R
for index in range(100):
    inputs=input().split()
    n1=int(inputs[0])
    n2=int(inputs[1])
    l=[]
    if n1<=0 or n2<=0:
        break
    elif n1<=n2:
        for i in range(n1,n2+1):
            l.append(i)
    elif n1>n2:
        for i in range(n2,n1+1):
            l.append(i)
    print('{} sum ={}'.format((str(l).replace('[','').replace(']','').replace(',','').replace("'",'')),(sum(l))))