a,b = map(int,input().split())
ba =[z for z in range(1,a+1)]
for _ in range(b):
    i,j=map(int,input().split())
    ba[i-1],ba[j-1]=ba[j-1],ba[i-1]
    
for m in range(a):
    print(ba[m],end=' ')