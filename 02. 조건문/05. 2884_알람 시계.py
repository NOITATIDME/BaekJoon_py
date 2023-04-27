A, B = map(int,input().split())

if B < 45:
    B += 60
    if A == 0:
        A = 23
    else:
        A -= 1

print(A ,B-45)
