# title : Coordinates of a Point
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/Q
inputs = input().split()
x = float(inputs[0])
y = float(inputs[1])
if x==0 and y==0:
    print('Origem')
elif x==0:
    print('Eixo Y')
elif y==0:
    print('Eixo X')
elif x>0 and y>0:
    print('Q1')
elif x<0 and y>0:
    print('Q2')
elif x<0 and y<0:
    print('Q3')
elif x>0 and y<0:
    print('Q4')