from secrets import token_bytes
 
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



def encrypt_b(path, key_path=None):

    f = open(path,'rb')
    encrypted, key = encryptBytes(f.read())
    f.close()

    f = open(path, 'w')
    f.write(str(encrypted))
    f.close()

    f=open(path+'.key','w')
    f.write(str(key))
    f.close()


def decrypte_b(path, key_path=None):

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



if __name__ == '__main__':

   #encrypt_b("img.jpg")
   decrypte_b("img.jpg","img.jpg.key")