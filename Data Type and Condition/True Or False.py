# title : True Or False?!
# Link : https://codeforces.com/group/usP2We5vrA/contest/278273/problem/P
inputs=input().split()
a=int(inputs[0])
b=int(inputs[1])
c=int(inputs[2])
d=int(inputs[3])
if b>c and d>a and sum([c,d])>sum([a,b]) and c>0 and d>0 and a%2==0:
    print('Accepted')
else:
    print('Error!')