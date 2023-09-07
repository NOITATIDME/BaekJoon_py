chess = [1,1,2,2,2,8]
chessSet = list(map(int, input().split()))
count = 0
for c in range(len(chess)):
    print((chess[c] - chessSet[count]), end = " ")
    count += 1