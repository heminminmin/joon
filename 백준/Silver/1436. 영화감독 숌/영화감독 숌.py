n = int(input())
apocalypse = 666
cnt = 0
while True:
    if '666' in str(apocalypse):
        cnt += 1
    if cnt == n:
        print(apocalypse)
        break
    apocalypse += 1