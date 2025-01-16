# title : Capital or Small or Digit
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/M
a=str(input())
if a.isalpha():
    print('ALPHA')
    if a.isupper():
        print('IS CAPITAL')
    else:
        print('IS SMALL')
elif a.isdigit():
    print('IS DIGIT')