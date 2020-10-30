#打印字母在单词中的出现频率 
def histotgram(word):
    d=dict()
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d

d =  histotgram('pneumonoultramicroscopicsilicovolcanoconiosis')
# {'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 't': 1, 'r': 2, 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}
print(d)