x, y = map(int, input().split())
a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
b = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
k=0
for i in range(x):
    k+=a[i]
k=(k+y)%7
print(b[k])