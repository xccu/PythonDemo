from Crypto.Cipher import AES
from Crypto import Random
import base64
import os
from rosetta_interface import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKC
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKC
from threading import Thread

#AES加密解密类
class AES_Encryptor(IEncryptor):
     #构造函数
    def __init__(self,callback=None):
        self.file_Util = Flie_Util()
        self.exception_util=Exception_Util()
        self.progress=0
        self.callback=callback
         # 密钥key必须为 16（AES-128）， 24（AES-192）， 32（AES-256）
        self.key = b'this is a 16 key'
        # 生成长度等于AES 块大小的不可重复的密钥向量
        self.iv = Random.new().read(AES.block_size)

    #生成密钥
    def create_key(self): 
        # 密钥key必须为 16（AES-128）， 24（AES-192）， 32（AES-256）
        self.key = b'this is a 16 key'
        # 生成长度等于AES 块大小的不可重复的密钥向量
        self.iv = Random.new().read(AES.block_size)
        
    #加密
    def encrypt(self,filepath):
        try:
            #bytes读取文件
            bytes_array=self.file_Util.read_file_stream(filepath,2048)
            # 使用 key 和iv 初始化AES 对象， 使用MODE_CFB模式
            self.mycipher = AES.new(self.key, AES.MODE_CFB, self.iv)

            # 分段加密
            en_bytes_array=[]
            i=0
            self.progress=0
            for bytes in bytes_array:
                i+=1
                self.setProgress(i,bytes_array)
                en_data = self.mycipher.encrypt(bytes)
                en_bytes_array.append(en_data)

            #写加密后的文件
            self.file_Util.write_file_stream(filepath,en_bytes_array)

            return "s_"
        except Exception as ex:
            return self.exception_util.print_exctption("encrypt",ex)

    #解密
    def decrypt(self,filepath):
        try:
            #bytes读取文件
            en_bytes_array=self.file_Util.read_file_stream(filepath,2048)
            # 解密需要用key 和iv 生成的AES对象
            mydecrypt = AES.new(self.key, AES.MODE_CFB, self.iv)

            # 分段解密
            bytes_array=[]
            i=0
            self.progress=0
            for bytes in en_bytes_array:
                i+=1
                self.setProgress(i,en_bytes_array)
                data = mydecrypt.decrypt(bytes)
                bytes_array.append(data)
        
            #写解密后的文件
            self.file_Util.write_file_stream(filepath,bytes_array)
            return "s_"
        except Exception as ex:
            return self.exception_util.get_exctption_info("decrypt",ex)
    
    #设置进度
    def setProgress(self,i,array):
        self.progress=(int)((i/len(array))*100)
        if self.callback is not None:
            self.callback(self.progress)

#RSA加密解密类
class RSA_Encryptor(IEncryptor):

    #构造函数
    def __init__(self,callback=None):
        self.file_Util = Flie_Util()
        self.exception_util=Exception_Util()
        self.progress=0
        self.callback=callback

    #创建RSA密钥对(公钥+私钥)
    def create_key(self):
        try:
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
            return "s_"
        except Exception as ex:
            return self.exception_util.print_exctption("create_rsa_key",ex)

    # 使用公钥对文件进行rsa 分段加密
    def encrypt(self,filepath):
        try:
            #bytes读取文件
            bytes_array=self.file_Util.read_file_stream(filepath,100)

            # 加载公钥
            rsa_key = RSA.import_key(open("client_public.pem").read() )

            # 分段加密
            en_bytes_array=[]
            cipher_rsa = Cipher_PKC.new(rsa_key)
            i=0
            self.progress=0
            for bytes in bytes_array:
                i+=1
                self.setProgress(i,bytes_array)
                en_data = cipher_rsa.encrypt(bytes)
                en_bytes_array.append(en_data)

            #写加密后的文件
            self.file_Util.write_file_stream(filepath,en_bytes_array)
            return "s_"
        except Exception as ex:
             return self.exception_util.get_exctption_info("encrypt",ex)
        

    # 使用私钥对文件进行rsa 分段解密
    def decrypt(self,filepath):
        try:
            #bytes读取文件
            en_bytes_array=self.file_Util.read_file_stream(filepath,128)

            # 读取私钥
            private_key = RSA.import_key(open("client_private.pem").read())

            # 分段解密
            bytes_array=[]
            cipher_rsa = Cipher_PKC.new(private_key)
            i=0
            self.progress=0
            for bytes in en_bytes_array:
                i+=1
                self.setProgress(i,en_bytes_array)
                data = cipher_rsa.decrypt(bytes,None)
                bytes_array.append(data)
        
            #写解密后的文件
            self.file_Util.write_file_stream(filepath,bytes_array)
            return "s_"
        except Exception as ex:
            return self.exception_util.get_exctption_info("decrypt",ex)
        
    #设置进度
    def setProgress(self,i,array):
        self.progress=(int)((i/len(array))*100)
        if self.callback is not None:
            self.callback(self.progress)


#文件读写类
class Flie_Util():
    #构造函数
    def __init__(self):
        self.exception_util=Exception_Util()
        self.s=""

    #读文件
    def read(self,filePath):
        try:
            print(filePath)
            f = open(filePath, 'r')
            result = f.read()
            print(result)
            return result
        except Exception as ex:
            return self.exception_util.get_exctption_info("read",ex)
        finally:
            if f:
                f.close()
    
    #写文件
    def write(self,filePath,data):
        try:
            print(filePath)
            f = open(filePath, 'w')
            f.write(data)
            f.write(bytes)
        except Exception as ex:
             self.exception_util.print_exctption("write",ex)
        finally:
            if f:
                f.close()

    #写字节
    def write_bytes(self,filePath,bytes):
        try:
            print(filePath)
            f = open(filePath, 'wb')
            f.write(bytes)
        except Exception as ex:
             self.exception_util.print_exctption("write_bytes",ex)
        finally:
            if f:
                f.close()

    #bytes分段读取文件
    def read_file_stream(self,filepath,length):
        bytes_array=[]
        try:
            f = open(filepath,'rb')
            while True:
                dt=f.read(length)
                if dt is not b'': #读取到结尾则结束
                    bytes_array.append(dt)
                    #print(dt)
                else:
                    break
        except Exception as ex:
             self.exception_util.print_exctption("read_file_stream",ex)
        finally:
            if f:
                f.close()
        return bytes_array

    #bytes列表写入文件
    def write_file_stream(self,filepath,bytes_array):
        try:
            f= open(filepath, 'wb')
            f.writelines(bytes_array)
        except Exception as ex:
             self.exception_util.print_exctption("write_file_stream",ex)
        finally:
            if f:
                f.close()
    
    #遍历指定文件夹中所有文件
    def foreach_folder(self,path):
        filelist=[]
        for root,dirs,files in os.walk(path):
            for name in files:
                path = os.path.join(root,name)
                filelist.append(path)
                print(path)
        return filelist
    
    def judge_path(self,path):
        if os.path.isdir(path):     #文件夹返回0
            print("文件夹"+path)
            return 0
        elif os.path.isfile(path):  #文件返回1
            print("文件"+path)
            return 1
        else:
            print("未识别"+path)
            return -1
 

class Exception_Util():
     #构造函数
    def __init__(self):
        self.s=""

    def print_exctption(self, msg,e):
        errorstr=self.get_exctption_info(msg,e)
        print(errorstr)

    def get_exctption_info(self,exStr, e):
        s='error:\t'
        s+=(exStr)
        s+=('\nstr(e):\t')
        s+=(str(e))
        s+=('\nrepr(e):\t')
        s+=(repr(e))
        return s
