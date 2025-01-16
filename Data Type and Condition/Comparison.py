# title : Comparison
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/V
inputs=input().split()
n1=int(inputs[0])
m=str(inputs[1])
n2=int(inputs[2])
if m=='>' and n1>n2:
    print('Right') 
elif m=='>' and n1<=n2:
        print('Wrong')
elif m=='=' and n1==n2:
    print('Right')
elif m=='=' and n1!=n2:
        print('Wrong')
elif m=='<' and n1<n2:
    print('Right')
elif m=='<' and n1>=n2:
        print('Wrong')