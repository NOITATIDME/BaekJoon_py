N, B = map(int,input().split())
tmp = ''
while N:
    tmp = str(N%B) + tmp
    N //= B

print(tmp)