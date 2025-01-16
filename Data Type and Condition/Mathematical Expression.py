# title : Mathematical Expression
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/W
inputs=input().split()
n1=int(inputs[0])
m=str(inputs[1])
n2=int(inputs[2])
eq='='
res=int(inputs[4])
if m=='+' and n1+n2==res:
    print('Yes') 
elif m=='+' and n1+n2!=res:
        print(n1+n2)
elif m=='-' and n1-n2==res:
    print('Yes')
elif m=='-' and n1-n2!=res:
        print(n1-n2)
elif m=='*' and n1*n2==res:
    print('Yes')
elif m=='*' and n1*n2!=res:
        print(n1*n2)