import base64
from Cryptodome.Cipher import AES

BS = 16
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]


class AESCipher:

    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = cipher.encrypt(raw)
        encrypted_data = base64.b64encode(enc)
        return encrypted_data

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted_data = unpad(cipher.decrypt(enc)).decode('utf-8')
        return decrypted_data
