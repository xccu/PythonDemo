#定义字典并赋初始值
word={
    'p': 2, 'n': 4, 'e': 1, 'u': 2, 'm': 2, 'o': 9, 'l': 3, 
    't': 1, 'r': 2, 'a': 2, 'i': 6, 'c': 6, 's': 4, 'v': 1}

#反转键值对的函数
def invert_dict(d):
    inverse=dict()
    for k in d:
        if d[k] not in inverse:
            inverse[d[k]] = [k] #原来的值不唯一，应定义为列表
        else:
            inverse[d[k]].append(k)
    return inverse

#{2: ['p', 'u', 'm', 'r', 'a'], 4: ['n', 's'], 1: ['e', 't', 'v'], 9: ['o'], 3: ['l'], 6: ['i', 'c']}
print(invert_dict(word)) 