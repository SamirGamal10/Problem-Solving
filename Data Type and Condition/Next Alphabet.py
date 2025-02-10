# Title : Next Alphabet
# Link :https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/C
a=input()
if a=='z':
    print(chr(ord(a) -25))
else:
    print(chr(ord(a)+1))