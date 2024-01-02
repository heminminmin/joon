A= []
N,M= map(int,input().split())
for k in range(1, N+1):
    A.append(k)
for q in range(M):
        i,j = map(int,input().split())
        A[i-1:j] = reversed(A[i-1:j])
print(*A)