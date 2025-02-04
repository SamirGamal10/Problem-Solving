# Title : Way Too Long Words
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/F
number_case=int(input())
for i in range(number_case):
    a=str(input())
    if len(a)<=10:
        print(a)
    else:
        print(f'{a[0]}{len(a)-2}{a[-1]}')