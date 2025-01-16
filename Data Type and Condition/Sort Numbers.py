# title : Sort Numbers
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/T
inputs=input().split()
a=int(inputs[0])
b=int(inputs[1])
c=int(inputs[2])
if a>=b>=c:
    print(c)
    print(b)
    print(a)
elif a>=c>=b:
    print(b)
    print(c)
    print(a)
elif b>=a>=c:
    print(c)
    print(a)
    print(b)
elif b>=c>=a:
    print(a)
    print(c)
    print(b)
elif c>=a>=b:
    print(b)
    print(a)
    print(c)
elif c>=b>=a:
    print(a)
    print(b)
    print(c)
print(end='\n')
print(a)
print(b)
print(c)