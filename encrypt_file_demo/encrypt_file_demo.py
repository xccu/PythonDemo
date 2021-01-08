from secrets import token_bytes
 
 #异或方式加密解密任意文件
def random_key(length):
    key = token_bytes(nbytes=length)
    key_int = int.from_bytes(key, 'big')
    return key_int

def encryptBytes(raw_bytes):
    raw_int = int.from_bytes(raw_bytes, 'big')
    key_int = random_key(len(raw_bytes))
    return raw_int ^ key_int, key_int

def decryptBytes(encrypted, key_int):
    decrypted = encrypted ^ key_int
    length = (decrypted.bit_length() + 7) // 8
    decrypted_bytes = int.to_bytes(decrypted, length, 'big') 
    return decrypted_bytes



def encrypt(path, key_path=None):
    
    f = open(path,'rb')
    encrypted, key = encryptBytes(f.read())
    f.close()

    f = open(path, 'w')
    f.write(str(encrypted))
    f.close()

    f=open(path+'.key','w')
    f.write(str(key))
    f.close()


def decrypt(path, key_path=None):

    f = open(path,'r')
    encrypted = int(f.read())
    f.close()

    f = open(key_path,'r')
    key = int(f.read())
    f.close()

    f = open(path, 'w')
    f.write(str(encrypted))
    f.close()

    decrypted = decryptBytes(encrypted, key)
    f = open(path, 'wb')
    f.write(decrypted)
    f.close()


def read_file_stream(filepath,length):
    bytes_array=[]
    with open(filepath,'rb') as f:
        while True:
            dt=f.read(length)
            if dt is not b'': #读取到结尾则结束
                bytes_array.append(dt)
                print(len(dt))
            else:
               break
    return bytes_array


if __name__ == '__main__':


    bytes_array=read_file_stream("url.txt",100)

    #f = open("img.jpg",'rb')

    #for line in f.read(100):                          #依次读取每行  
    #    bytes_array.append(line)
    #    print("{}".format(line))
    print(len(bytes_array))


    f = open("url1.txt", 'wb')
    f.writelines(bytes_array)
    f.close()

   #encrypt("img.jpg")
   #decrypt("img.jpg","img.jpg.key")