# title : Calculator
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/O
eq = input()
for a in eq:
    if a in '+-*/':
        m=a
        inputs=eq.split(m)
n1=int(inputs[0])
n2=int(inputs[1])
if m=='+':
    print(n1+n2)
elif m=='-':
    print(n1-n2)
elif m=='*':
    print(n1*n2)
elif m=='/':
    print(n1//n2)