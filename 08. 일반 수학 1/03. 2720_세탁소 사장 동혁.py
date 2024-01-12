T = int(input())

for _ in range(T):
    C = int(input())
    result = []
    for M in [25,10,5,1]:
        result.append(C//M)
        C = C%M
    print(*result)