try:
    x=float(input('请输入被除数：'))
    y=float(input('请输入除数：'))
    print('{}/{}={}'.format(x,y,x/y))
except ZeroDivisionError:
    #ZeroDivisionError异常
    print('除数不能为0')
except ValueError:
    #ValueError异常
    print('被除数和除数必须是数字')
else:
   print('程序正确运行')
finally:
    #无论是否异常都最后执行
    print('程序结束')