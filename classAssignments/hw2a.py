#hw2a

words = ['fellowing', 'love', 'program', 'machines', 'learning', 'python', 'air', 'supercalifragilisticexpialidious', 'aaaaaaaaaaa']

for word in words:

    if word[0] == 'a' and len(word) < 5:
        print("1", word)
    elif ('e' in word or 'o' in word) and len(word) > 7:
        print("2", word)
    elif len(word) > 10:
        print("3", word)


# 2
# 2
# 2
# 2
# 1
# 2
# 3
