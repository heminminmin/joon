a,b=map(int,input().split())
ba= []
for m in range(a):
    ba.append(0)

for h in range(b):
    i,j,k= map(int,input().split())
    for z in range(i-1,j):
        ba[z]=k

for q in range(a):
    print(ba[q],end=' ')
