a,b,c = list(map(int,input().split()))


if (a == b) and  (b== c) and (c==a):
    print(10000 + a * 1000)
elif (a==b):
    print(a*100 +1000)
elif (a==c):
    print(a*100+1000)
elif b==c: 
    print(c*100+1000)
else:
    print(max(a,b,c)*100)