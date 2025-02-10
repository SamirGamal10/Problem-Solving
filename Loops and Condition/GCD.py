# Title : GCD
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/L
inputs=input().split()
n1=int(inputs[0])
n2=int(inputs[1])
l_n1=[]
l_n2=[]
for i in range(1,n1+1):
    if str(n1/i).split('.')[1]=='0':
        l_n1.append(i)
for j in range(1,n2+1):
    if str(n2/j).split('.')[1]=='0':
        l_n2.append(j)
print(max(set(l_n1) & set(l_n2)))