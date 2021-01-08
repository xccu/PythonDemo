from Crypto.Cipher import AES
from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKC
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKC

#AES加密解密类
class AES_Util():
     #构造函数
    def __init__(self):
        # 密钥key必须为 16（AES-128）， 24（AES-192）， 32（AES-256）
        self.key = b'this is a 16 key'
        
    def encrypt(self,dataStr):
        # 生成长度等于AES 块大小的不可重复的密钥向量
        self.iv = Random.new().read(AES.block_size)
        # 使用 key 和iv 初始化AES 对象， 使用MODE_CFB模式
        self.mycipher = AES.new(self.key, AES.MODE_CFB, self.iv)
        # 将iv(密钥向量)加到加密的密钥开头， 一起返回
        ciptext =self.iv + self.mycipher.encrypt(dataStr.encode())
        print(ciptext)
        return ciptext

    def decrypt(self,ciptext):
        # 解密需要用key 和iv 生成的AES对象
        mydecrypt = AES.new(self.key, AES.MODE_CFB, ciptext[:16])
        # 使用新生成的AES 对象， 将加密的密钥解密
        text = mydecrypt.decrypt(ciptext[16:]).decode()
        print(text)
        return text

#RSA加密解密类
class RSA_Util():
    #构造函数
    def __init__(self):
        self.file_Util = Flie_Util()

    #创建RSA密钥对(公钥+私钥)
    def create_rsa_key(self):

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

    # 使用公钥对文件进行rsa 分段加密
    def encrypt(self,filepath):

        #bytes读取文件
        bytes_array=self.file_Util.read_file_stream(filepath,100)

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
        self.file_Util.write_file_stream(filepath,en_bytes_array)

    # 使用私钥对文件进行rsa 分段解密
    def decrypt(self,filepath):

        #bytes读取文件
        en_bytes_array=self.file_Util.read_file_stream(filepath,128)

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
        self.file_Util.write_file_stream(filepath,bytes_array)

#文件读写类
class Flie_Util():
     #构造函数
    def __init__(self):
        self.s=""

    #读文件
    def read(self,filePath):
        try:
            print(filePath)
            f = open(filePath, 'r')
            result = f.read()
            print(result)
            return result
        except:
             print("Error")
             return ""
        finally:
            if f:
                f.close()
    
    #写文件
    def write(self,filePath,data):
        try:
            print(filePath)
            f = open(filePath, 'w')
            f.write(data)
        except:
             print("Error in write")
        finally:
            if f:
                f.close()

    #写字节
    def writeBytes(self,filePath,bytes):
        try:
            print(filePath)
            f = open(filePath, 'wb')
            f.write(bytes)
        except:
             print("Error in writeBytes")
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
        except:
             print("Error in read_file_stream")
        finally:
            if f:
                f.close()
        return bytes_array

    #bytes列表写入文件
    def write_file_stream(self,filepath,bytes_array):
        try:
            f= open(filepath, 'wb')
            f.writelines(bytes_array)
        except:
             print("Error in write_file_stream")
        finally:
            if f:
                f.close()