# Title : Print
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/B
n=int(input())
def PrintFromOneTONumber(n):
    numbers=list(range(1,n+1))
    print(str(numbers).replace('[','').replace(']','').replace(',',''))
PrintFromOneTONumber(n)