# title : Sum of Consecutive Odd Numbers
# Link : https://codeforces.com/group/usP2We5vrA/contest/278275/problem/L
n1=int(input())
for i in range(1,n1+1):
    count=0
    inputs=input().split()
    x=int(inputs[0])
    y=int(inputs[1])
    if x==y or x==y+1 or x==y-1:
        print(0)
    elif x<y:
        for i2 in range(x+1,y):
            if i2%2==1:
                count+=i2
        print(count)
            
    elif x>y:
        for i2 in range(y+1,x):
            if i2%2==1:
                count+=i2
        print(count)