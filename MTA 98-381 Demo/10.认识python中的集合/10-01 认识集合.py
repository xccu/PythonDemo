#集合{} 列表[] 元组()
name = ['zweig','tom','zweig','mary','hofmann','merkel','mike','tom']

#s=set()定义空集合，s={}被认为是空字典 <class 'dict'>
s=set()
#打印  <class 'set'>
print(type(s))

#列表转换为集合并去重（集合无序且不允许重复）
s=set(name)
#随机顺序打印 {'hofmann', 'merkel', 'tom', 'mike', 'mary', 'zweig'}
print(s)
#乱序打印
print(set('python'))
