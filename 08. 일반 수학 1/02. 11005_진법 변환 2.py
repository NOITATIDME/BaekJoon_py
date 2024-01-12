N, B = map(int,input().split())
tmp = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N:
    tmp += str(arr[N%B])
    N //= B

print(tmp[::-1])