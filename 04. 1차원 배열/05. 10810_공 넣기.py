N, M = map(int,input().split())

data = [0 for _ in range(N)]

for _ in range(M):
    I, J, K = map(int,input().split())
    for n in range(I, J+1):
        data[n-1] = K

for i in range(N):
    print(data[i], end=" ")