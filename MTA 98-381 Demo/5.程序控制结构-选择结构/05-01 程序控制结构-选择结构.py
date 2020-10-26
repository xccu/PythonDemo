#使用input输入str类型变量并转换为int类型
#提示信息 请输入成绩：
score=int(input('请输入成绩：')) 

#if语句
if score<60 and score>=0:
    print('不及格')
#else:
#    print('及格')
elif score>=60 and score<75:
    print('及格')
elif score>=75 and score<85:
    print('良好')
elif score>=85 and score<=100:
    print('优秀')
else:
    print('输入错误，请检查')