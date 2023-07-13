a,b =map(int,input().split())
l =[]
c = list(map(int,input().split()))
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if (c[i]+c[j]+c[k] <= b): 
                l.append(c[i]+c[j]+c[k])
print(max(l))