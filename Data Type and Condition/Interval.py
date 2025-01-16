# title : Interval
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/S
inputs = input().split()
number = float(inputs[0])
a='Interval [0,25]'
b='Interval (25,50]'
c='Interval (50,75]'
d='Interval (75,100]'
e='Out of Intervals'
if 0<=number<=25:
    print(a)
elif 25.1<=number<=50:
    print(b)
elif 50.1<=number<=75:
    print(c)
elif 75.1<=number<=100:
    print(d)
else:
    print(e)
