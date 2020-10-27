#def定义函数
def print_songs():
    print('Do you hear the people sing!')

#使用函数
print_songs()

#注意顺序 先定义函数才能调用
def repeat_songs():
    print_songs()
    print_songs()

repeat_songs()