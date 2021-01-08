#RSA分段加密解密文件Demo

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKC
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKC

#创建RSA密钥对(公钥+私钥)
def create_rsa_key():
    """
    步骤说明：
    1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码
    2、生成 1024/2048 位的 RSA 密钥
    3、调用 RSA 密钥实例的 exportKey 方法，传入密码、使用的 PKCS 标准以及加密方案这三个参数。
    4、将私钥写入磁盘的文件。
    """

    # 伪随机数生成器
    random_gen = Random.new().read
    # 生成秘钥对实例对象：1024是秘钥的长度
    rsa = RSA.generate(1024, random_gen)

    # 秘钥对的生成
    private_pem = rsa.exportKey()
    with open("client_private.pem", "wb") as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open("client_public.pem", "wb") as f:
        f.write(public_pem)

#bytes分段读取文件
def read_file_stream(filepath,length):
    bytes_array=[]
    with open(filepath,'rb') as f:
        while True:
            dt=f.read(length)
            if dt is not b'': #读取到结尾则结束
                bytes_array.append(dt)
                #print(dt)
            else:
               break
    return bytes_array

#bytes写入文件
def write_file_stream(filepath,bytes_array):
    with open(filepath, 'wb') as f:
        f.writelines(bytes_array)

# 使用公钥对文件进行rsa 分段加密
def encrypt(filepath):

    #bytes读取文件
    bytes_array=read_file_stream(filepath,100)

    # 加载公钥
    rsa_key = RSA.import_key(open("client_public.pem").read() )

    # 分段加密
    en_bytes_array=[]
    cipher_rsa = Cipher_PKC.new(rsa_key)
    for bytes in bytes_array:
        en_data = cipher_rsa.encrypt(bytes)
        #print(len(en_data))
        en_bytes_array.append(en_data)

    #写加密后的文件
    write_file_stream(filepath,en_bytes_array)

# 使用私钥对文件进行rsa 分段解密
def decrypt(filepath):

    #bytes读取文件
    en_bytes_array=read_file_stream(filepath,128)

    # 读取私钥
    private_key = RSA.import_key(open("client_private.pem").read())

    # 分段解密
    bytes_array=[]
    cipher_rsa = Cipher_PKC.new(private_key)
    for bytes in en_bytes_array:
        data = cipher_rsa.decrypt(bytes,None)
        #print(len(data))
        bytes_array.append(data)
        
    #写解密后的文件
    write_file_stream(filepath,bytes_array)


if __name__ == '__main__':
    
    #create_rsa_key()

    #encrypt('img.jpg')
    decrypt('img.jpg')