word = input().upper()
charWord = list(set(word))

cnt_list = []
for i in charWord:
    count = word.count(i)
    cnt_list.append(count)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(charWord[cnt_list.index(max(cnt_list))])