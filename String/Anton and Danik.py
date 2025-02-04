# Title : Anton and Danik
# Link : https://codeforces.com/contest/734/problem/A?outsideGroup=true
l = []
number=int(input())
A=str(input())
for i in list(A):
    l.append(i)
l=l[0:number]
if l.count("A")>l.count("D"):
    print('Anton')
elif l.count("A")<l.count("D"):
    print('Danik')
elif l.count("A")==l.count("D"):
    print('Friendship')