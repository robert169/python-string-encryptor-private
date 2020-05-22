class encryptor:
    
    def __init__(self):
        self.encrypted = b"l+N#GC?oOTMcPQ^nXB,Ek(w@;_frLy=/iVqKjhg$[*vJsb&Z)!}xam-YeuHI:R.pDSFzt{dxUA]"
        self.decrypted = b"();:/?!@#${}^&*+_-=,.[]ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqxrstuvwxyz"
        self.encrypt_table = bytes.maketrans(self.decrypted, self.encrypted)
        self.decrypt_table = bytes.maketrans(self.encrypted, self.decrypted)
    
    def decrypt(self, message, secret, random):
        return message.translate(self.decrypt_table)
    
    def encrypt(self, message, secret, random):
        return message.translate(self.encrypt_table)
        
