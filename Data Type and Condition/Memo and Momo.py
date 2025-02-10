# Title : Memo and Momo
# Link : https://codeforces.com/group/MWSDmqGsZm/contest/326175/problem/B
inputs=input().split()
memo=int(inputs[0])
momo=int(inputs[1])
k=int(inputs[2])
if int(str(memo/k).split('.')[1])==0 and int(str(momo/k).split('.')[1])==0:
    print('Both')
elif int(str(memo/k).split('.')[1])!=0 and int(str(momo/k).split('.')[1])!=0:
    print('No One')
elif int(str(memo/k).split('.')[1])==0:
    print('Memo')
elif int(str(momo/k).split('.')[1])==0:
    print('Momo')