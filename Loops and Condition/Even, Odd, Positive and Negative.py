# title : Even, Odd, Positive and Negative
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/C
n1 = int(input())
n2 = list(map(int, input().split()))
evencount=0
oddcount=0
postivecount=0
nagativecount=0
for number in n2:
    if number%2==0:
        evencount+=1
    else:
        oddcount+=1

    if number>0:
        postivecount+=1
    elif number<0:
        nagativecount+=1
print(f'Even: {evencount}')
print(f'Odd: {oddcount}')
print(f'Positive: {postivecount}')
print(f'Negative: {nagativecount}')