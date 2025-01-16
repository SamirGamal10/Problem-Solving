# title : Two numbers
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/H
import math
inputs = input().split()
A=int(inputs[0])
B=int(inputs[1])
print(f"floor {A} / {B} = {math.floor (A / B)}")
print(f"ceil {A} / {B} = {math.ceil (A / B)}")
if '.5' in str(A / B):
    print(f"round {A} / {B} = {math.ceil (A / B)}")
else:
    print(f"round {A} / {B} = {round(A / B)}")