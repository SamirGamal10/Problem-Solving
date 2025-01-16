# title : Age in Days
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/R
number=int(input())
years=number//365
number=number-years*365
month=number//30
number=number-month*30
day=number
print(f'{years} years')
print(f'{month} months')
print(f'{day} days')