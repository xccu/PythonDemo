#流读取文件
#https://blog.csdn.net/sswai/article/details/106395897

def read_file_stream(filepath,length):
    bytes_array=[]
    with open(filepath,'rb') as f:
        while True:
            dt=f.read(length)
            if dt is not b'': #读取到结尾则结束
                bytes_array.append(dt)
                print("{}".format(dt))
            else:
               break
    return bytes_array

def write_file_stream(filepath,bytes_array):
    with open(filepath, 'wb') as f:
        f.writelines(bytes_array)


if __name__ == '__main__':
    bytes_array = read_file_stream('img.jpg',100)
    print(len(bytes_array))
    write_file_stream('img1.jpg',bytes_array)

