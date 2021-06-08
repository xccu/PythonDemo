#多线程输出
import threading
import _thread
import time

threadLock = threading.Lock()
dict_data={}

def write_string(no,path="test.txt"):
    time.sleep(5)
    count=0
    i=0
    while i <= no:
        count += (i)
        i+=1
    print(str(no)+":\t"+str(count))
    dict_data[no] = str(no)+":\t"+str(count)+'\n'

# 创建新线程
print('开始')
# 创建线程列表
threads = []
for i in range(1,1001):
    t = threading.Thread(target=write_string, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()
print("所有线程任务完成")

# 按照字典的key排序输出
list_data=[]
for i in sorted (dict_data) : 
    list_data.append(dict_data[i])

with open('test.txt', 'a') as f:
    f.writelines(list_data )