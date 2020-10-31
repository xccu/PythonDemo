name = ['zweig','tom','zweig','mary','hofmann','merkel','mike','tom']
name_s=set(name)
#{'zweig', 'mike', 'mary', 'merkel', 'tom', 'hofmann'}
print(name_s)

#判断元素是否在集合中 打印 True False
print('zweig' in name_s,'Zweig' in name_s)
#判断集合长度 打印 6
print(len(name_s))

#集合添加元素
name_s.add('noche')
name_s.add('zweig')
#重复元素不会添加 打印 {'zweig', 'hofmann', 'tom', 'noche', 'mary', 'mike', 'merkel'}
print(name_s)

#集合删除元素，如果删除了不存在的元素会报异常
name_s.remove('noche')
#打印 {'tom', 'mike', 'mary', 'merkel', 'zweig', 'hofmann'}
print(name_s)
#discard 删除了不存在的元素不会报异常
name_s.discard('zweig')
name_s.discard('zweig')
#打印 {'tom', 'hofmann', 'merkel', 'mike', 'mary'}
print(name_s)

#从集合中随机弹出一个元素（可用于生成随机数）
print(name_s.pop())

#清空集合
name_s.clear()
#打印 set()
print(name_s)