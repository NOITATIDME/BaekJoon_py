A, B = map(int,input().split())
if B > 45:
    B -= 45
elif B < 45:
    if A == 0:
        B += 60
        B -= 45
        A = 23
    else:
        B += 60
        B -= 45
        A -= 1

print(A ,B)
