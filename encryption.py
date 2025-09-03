class Encrption:
    @staticmethod
    def encrypt(data,key):
        result = ""
        i = 0
        while len(data) > i:
            for char in key:
                if i < len(data):
                    result += chr(ord(data[i]) ^ ord(char))
                    i += 1
                else:
                    break
        return result
    def decrypt(data,key):
        return Encrption.encrypt(data,key)
    


            


