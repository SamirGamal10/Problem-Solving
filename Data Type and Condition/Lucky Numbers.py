# Title : Lucky Numbers
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/I
number=(input())
if ((str(number)[0])=='0' or str(number)[1]=='0') :
    print('NO')
elif str(int((str(number)[0])) / int((str(number)[1]))).split('.')[1]=='0' or str(int((str(number)[1])) / int((str(number)[0]))).split('.')[1]=='0':
    print('YES')
else:
    print('NO')