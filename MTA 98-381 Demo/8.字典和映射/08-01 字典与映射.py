#创建字典
names=dict()
print(names)

#添加键值对
names['one']='mike'
# {'one': 'mike'}
print(names)

names['two']='sweig'
names['three']='hofmann'
# {'one': 'mike', 'two': 'sweig', 'three': 'hofmann'}
print(names)
#字典长度 打印 3
print(len(names))

# 修改键为'three'的值
names['three']='merkel'
# {'one': 'mike', 'two': 'sweig', 'three': 'merkel'}
print(names)

# 判断键是否在字典中 打印 True
print('one' in names) #也可以用 'one' in names.keys()
# 判断值是否在字典中 打印 True
print('merkel' in names.values())