# Title : Reverse Words
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q
l=[]
s=str(input())
words=s.split(' ')
for word in words:
    word=word[::-1]
    l.append(word)
print(str(l).replace(']','').replace('[','').replace(',','').replace("'",''))