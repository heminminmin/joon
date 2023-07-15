#색종이 2563
#100*100 , 2차원 리스트 선언 
paper =[[0 for _ in range(100)] for _ in range (100)]
n=int(input())
for i in range(n):
    left , bottom = map(int,input().split())
    for y in range(left, left+10):
        for x in range(bottom, bottom+10):
            paper[y][x] =1
count=0    
for y in range(100):
    for x in range(100):
        if paper[y][x] ==1 :
            count +=1 
            
print(count)   
        