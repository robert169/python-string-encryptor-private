class encryptor:
    
    def __init__(self):
        self.encrypted = b"l+N#GC?oOTMcPQ^nXB,Ek(w@;_frLy=/iVqKjhg$[*vJsb&Z)!}xam-YeuHI:R.pDSFzt{dxUA]"
        self.decrypted = b"();:/?!@#${}^&*+_-=,.[]ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqxrstuvwxyz"
        self.encrypt_table = bytes.maketrans(self.decrypted, self.encrypted)
        self.decrypt_table = bytes.maketrans(self.encrypted, self.decrypted)
    
    def decrypt(self, message, watermark, secret, random):
        if watermark == "Made by roberth#0310":
            return message.translate(self.decrypt_table)
        else:
            return "File was modified, breaking process | Made by roberth#0310"

    def encrypt(self, message, watermark,secret, random):
        if watermark == "Made by roberth#0310":
            return message.translate(self.encrypt_table)
        else:
            return "File was modified, breaking process | Made by roberth#0310"
        
