S = input()
alphabet = [chr(code) for code in range(97,123)]

for i in alphabet:
    if i in S:
        print(S.index(i), end = " ")
    else:
        print(-1, end = " ")