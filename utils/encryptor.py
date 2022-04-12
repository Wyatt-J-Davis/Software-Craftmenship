from cryptography.fernet import Fernet

class Encryptor(object):
    def __init__(self):
        self._key = Fernet.generate_key()

    def encrypt(self, value):
        return Fernet(self._key).encrypt(bytes(value, encoding='utf-8'))
    
    def decrypt(self, token):
        return Fernet(self._key).decrypt(token).decode("utf-8")
