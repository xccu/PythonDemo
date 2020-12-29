#装饰器demo
def a_new_decorator(a_func):
 
    def wrapTheFunction():
        print("执行函数 a_func() 开始")
        a_func()
        print("执行函数 a_func() 结束")
    return wrapTheFunction
 
@a_new_decorator
def a_function_requiring_decoration():
    print("执行中...")
 
#outputs: 执行函数 a_func() 开始
#         执行中...
#         执行函数 a_func() 结束
a_function_requiring_decoration()
 
#the @a_new_decorator is just a short way of saying:
#a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# 输出函数名称，这里的函数被warpTheFunction重写了
# Output: wrapTheFunction
print(a_function_requiring_decoration.__name__)