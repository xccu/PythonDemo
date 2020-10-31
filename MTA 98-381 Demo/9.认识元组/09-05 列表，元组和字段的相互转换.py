name = ['zwzig','tom','mary','hofmann','merkel','mike']

#列表转换为元组
name_t=tuple(name)
#('zwzig', 'tom', 'mary', 'hofmann', 'merkel', 'mike')
print(name_t)

#元组转换为列表
#['zwzig', 'tom', 'mary', 'hofmann', 'merkel', 'mike']
print(list(name_t))

name_score=[('zwzig',90),('tom',88),
            ('mary',95),('hofmann',78),
            ('merkel',82),('mike',85)]

#元组转换为字典
d = dict(name_score)
print(d)

#字典转换为元组（列表嵌套的元组）
#dict_items([('zwzig', 90), ('tom', 88), ('mary', 95), ('hofmann', 78), ('merkel', 82), ('mike', 85)])
print(d.items())

t=list(d.items())
#[('zwzig', 90), ('tom', 88), ('mary', 95), ('hofmann', 78), ('merkel', 82), ('mike', 85)] 
print(t)