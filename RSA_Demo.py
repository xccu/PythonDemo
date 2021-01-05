#RSA加密解密Demo

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKC
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5 as Signature_PKC

class HandleRSA():
    def create_rsa_key(self):
        """

        创建RSA密钥

        步骤说明：

        1、从 Crypto.PublicKey 包中导入 RSA，创建一个密码

        2、生成 1024/2048 位的 RSA 密钥

        3、调用 RSA 密钥实例的 exportKey 方法，传入密码、使用的 PKCS 标准以及加密方案这三个参数。

        4、将私钥写入磁盘的文件。

        5、使用方法链调用 publickey 和 exportKey 方法生成公钥，写入磁盘上的文件。

        """
        # 伪随机数生成器
        random_gen = Random.new().read
        # 生成秘钥对实例对象：1024是秘钥的长度
        rsa = RSA.generate(1024, random_gen)

        # Server的秘钥对的生成
        private_pem = rsa.exportKey()
        with open("server_private.pem", "wb") as f:
            f.write(private_pem)

        public_pem = rsa.publickey().exportKey()
        with open("server_public.pem", "wb") as f:
            f.write(public_pem)

        # Client的秘钥对的生成
        private_pem = rsa.exportKey()
        with open("client_private.pem", "wb") as f:
            f.write(private_pem)

        public_pem = rsa.publickey().exportKey()
        with open("client_public.pem", "wb") as f:
            f.write(public_pem)

    # Server使用Client的公钥对内容进行rsa 加密
    def encrypt(self, plaintext):
        """
        client 公钥进行加密
        plaintext:需要加密的明文文本，公钥加密，私钥解密
        """

        # 加载公钥
        rsa_key = RSA.import_key(open("client_public.pem").read() )

        # 加密
        cipher_rsa = Cipher_PKC.new(rsa_key)
        en_data = cipher_rsa.encrypt(plaintext.encode("utf-8")) # 加密

        # base64 进行编码
        base64_text = base64.b64encode(en_data)

        return base64_text.decode() # 返回字符串

    # Client使用自己的私钥对内容进行rsa 解密
    def decrypt(self, en_data):
        """
        en_data:加密过后的数据，传进来是一个字符串
        """
        # base64 解码
        base64_data = base64.b64decode(en_data.encode("utf-8"))

        # 读取私钥
        private_key = RSA.import_key(open("client_private.pem").read())

        # 解密
        cipher_rsa = Cipher_PKC.new(private_key)
        data = cipher_rsa.decrypt(base64_data,None)

        return data.decode()

    # Server使用自己的私钥对内容进行签名
    def signature(self,data:str):
        """
         RSA私钥签名
        :param data: 明文数据
        :return: 签名后的字符串sign
        """


        # 读取私钥
        private_key = RSA.import_key(open("server_private.pem").read())
        # 根据SHA256算法处理签名内容data
        sha_data= SHA256.new(data.encode("utf-8")) # b类型

        # 私钥进行签名
        signer = Signature_PKC.new(private_key)
        sign = signer.sign(sha_data)

        # 将签名后的内容，转换为base64编码
        sign_base64 = base64.b64encode(sign)
        return sign_base64.decode()

    # Client使用Server的公钥对内容进行验签

    def verify(self,data:str,signature:str) -> bool:
        """
        RSA公钥验签
        :param data: 明文数据,签名之前的数据
        :param signature: 接收到的sign签名
        :return: 验签结果,布尔值
        """
        # 接收到的sign签名 base64解码
        sign_data = base64.b64decode(signature.encode("utf-8"))

        # 加载公钥
        piblic_key = RSA.importKey(open("server_public.pem").read())

        # 根据SHA256算法处理签名之前内容data
        sha_data = SHA256.new(data.encode("utf-8"))  # b类型

        # 验证签名
        signer = Signature_PKC.new(piblic_key)
        is_verify = signer.verify(sha_data, sign_data)

        return is_verify

if __name__ == '__main__':

    mrsa = HandleRSA()
    #mrsa.create_rsa_key()
    e = mrsa.encrypt('hello client, this is a message')
    d = mrsa.decrypt(e)
    print(e)
    print(d)
    #---------------------------------
    sign_data = mrsa.signature("我叫阿登哥")
    is_verify = mrsa.verify(data="我叫阿登哥",signature=sign_data)
    print("签名：\n",sign_data)
    print("验签：\n",is_verify)

    """
    总结
    Pycrypto提供了比较完善的加密算法。RSA广泛用于加密与解密，还有数字签名通信领域。使用Publick/Private秘钥算法中，
    加密主要用对方的公钥，解密用自己的私钥。签名用自己的私钥，验签用对方的公钥。

    - 加密解密：公钥加密，私钥解密
    - 签名验签：私钥签名，公钥验签

    无论是加密解密还是签名验签都使用同一对秘钥对
    """