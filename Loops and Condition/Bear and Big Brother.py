# Title : Bear and Big Brother
# Link : https://codeforces.com/contest/791/problem/A
inputs=input().split()
Limak=int(inputs[0])
Bob=int(inputs[1])
a=0
while Limak<=Bob:
    Limak=Limak*3
    Bob=Bob*2
    a+=1
print(a)