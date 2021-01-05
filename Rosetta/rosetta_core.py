from Crypto.Cipher import AES
from Crypto import Random


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