from functools import wraps
 
def a_new_decorator(a_func):
    @wraps(a_func) #在装饰器里面访问在装饰之前的函数的属性
    def wrapTheFunction():
        print("执行函数 a_func() 开始")
        a_func()
        print("执行函数 a_func() 结束")
    return wrapTheFunction
 
@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("执行中...")
 
# Output: a_function_requiring_decoration
print(a_function_requiring_decoration.__name__)
