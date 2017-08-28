form Crypto.Cipher import AES

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xc4\x94\x9d(\x9e[EX\xc8\xbfI{\xa2$\x05\x18'
message = input("Entre your message:")
cipher = AES.new(key)

def pad(s):
    return s +((16-len(s)%16)*'{')

def encrypt(plaintext):
    global cipher
    return cipher.encrypt(pad(plaintext))

def decrypt(ciphertext):
    global cipher
    dec = cipher.decrypt((ciphertext).decode('utf-8'))
    l = dec.count('{')
    return dec[:len(dec)-l]

print("Your message:",message)
encrypted = encrypt(message)
decrypted = decrypt(message)
print("your encrypted messgae:",encrypted)
print("your encrypted messgae:",decrypted)