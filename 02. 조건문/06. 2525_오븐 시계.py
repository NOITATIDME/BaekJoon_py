H, M = map(int, input().split())
M1 = int(input())

if M + M1 > 60:
    M -= 60
    if H == 23:
        H = 0
    else:
        H += 1

print(H, M+M1)