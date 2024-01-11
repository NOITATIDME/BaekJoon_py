word = []
for i in range(5):
    word.append(input())

for j in range(15):
    for k in range(5):
        if(j < len(word[k])):
            print(word[k][j],end = "")