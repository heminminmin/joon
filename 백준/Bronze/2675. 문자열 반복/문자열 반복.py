t=int(input())
for _ in range (1,t+1):
    r, s = input().split()
    s= str(s)
    # print(list(r))
    for i in range(len(s)):
        print(int(r)*s[i],end = "")
    print()
