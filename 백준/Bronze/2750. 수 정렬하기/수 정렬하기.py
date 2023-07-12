a = int(input())
b=[] 
for i in range(a):
    b.append(int(input()))

b.sort()
for k in range(a):
    print(b[k],sep=' ')