price = int(input())
number = int(input())
total=0
for _ in range(number):
    a ,b =map(int,input().split())
    total += a*b 

if total==price :
    print('Yes')
else:
    print('No')
