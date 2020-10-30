#定义字典并赋初始值
word={
    'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 
    't': 1, 'r': 2, 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}

#sorted迭代器，按照键升序排序
for c in sorted(word):
    print('{}:{}'.format(c,word[c]))

#sorted迭代器，reverse=True 按照键降序排序
for c in sorted(word,reverse=True):
    print('{}:{}'.format(c,word[c]))