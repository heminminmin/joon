k = int(input())

a = 0
b= 1
for i in range (0,k):
     a,b= b, a+b
     
print(a)