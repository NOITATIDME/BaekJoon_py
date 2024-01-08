A = []
for i in range(9):
    a = list(map(int, input().split()))
    A.append(a)

max_value = max(map(max, A))

index = 0
for i in A:
    i.find(max_value)