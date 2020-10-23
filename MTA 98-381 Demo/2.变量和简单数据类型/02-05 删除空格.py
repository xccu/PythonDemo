full_name=' charlie xie '

print(full_name)
#删除左边的空格
print(full_name.lstrip())
#删除右边的空格
print(full_name.rstrip())
#删除两侧的空格
print(full_name.strip())

#变量本身没有改变
print(full_name)

#永久删除两侧空格
full_name = full_name.strip()
print(full_name)