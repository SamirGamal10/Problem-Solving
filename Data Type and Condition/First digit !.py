# title : First digit !
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/P
number=int(input())
len(str(number))
if len(str(number))==3:
    if (number//100)%2==0:
      print('EVEN')
    else:
      print('ODD')
elif len(str(number))==4:
    if (number//1000)%2==0:
      print('EVEN')
    else:
      print('ODD')