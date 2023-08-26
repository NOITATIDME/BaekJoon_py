count = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    print('Case #' + str(count) + ': ' + str(a + b))
    count += 1