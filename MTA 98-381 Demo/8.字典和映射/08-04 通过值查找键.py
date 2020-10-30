#定义字典并赋初始值
word={
    'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 
    't': 1, 'r': 2, 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}

#查找指定值的键
def reverse_lookup(d,v):
    result=[]
    for c in d:
        if d[c]==v:
            result.append(c)
    return result
# ['e', 't', 'v']
print(reverse_lookup(word,1))