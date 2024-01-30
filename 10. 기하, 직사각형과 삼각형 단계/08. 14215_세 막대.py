list = sorted(list(map(int, input().split())))

if list[2] < list[1] + list[0]:
    print(sum(list))
else:
    print((list[0] + list[1]) * 2 - 1)