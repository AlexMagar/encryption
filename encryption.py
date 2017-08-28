

'''
#encryption type 1
letters = {'a':'e', 'b':'d', 'c':'r', 'd':'c', 'e':'h', 'f':'p', 'g':'z', 'h':'u', 'i':'g',
           'j':'f', 'k':'o', 'l':'i', 'm':'s', 'n':'l', 'o':'b', 'p':'w', 'q':'m', 'r':'v',
           's':'j', 't':'y', 'u':'k', 'v':'q', 'w':'x', 'x':'t', 'y':'n', 'z':'a'
           }
message = input("entre your message: ").lower()
encrypted = ""

for letter in message:
    if letter in letters:
        encrypted += letters[letter]
    else:
        encrypted +=letter
print(encrypted)
'''
'''
#encryption type 2
alpha = "abcdefghijklmnopqrstuvwxyz"

message1 = input("entre the message: ").lower()
encrypted1 =""

for letter1 in message1:
    if letter1 == " ":
        encrypted1 += letter1
    elif alpha.index(letter1) + 5 >= len(alpha):
        encrypted1 += alpha[alpha.index(letter1) + 5 - 26]
     #   print(encrypted1)
      #  print("your string is mero than enough")
    else:
        encrypted1 += alpha[alpha.index(letter1) + 5 ]
print(encrypted1)
print(alpha.index('b')) #checks the position of input letter in alpha

#decryption type 2
EncryptedText = encrypted1
decryption1 =""
for letter2 in EncryptedText:
    if letter2 == " ":
        decryption1 += letter2
     #   print("there is space")
    elif alpha.index(letter2) - 5 < alpha.index('a'):
        print(alpha.index(letter2) - 5 + 26) #give the inxed of letter2
        decryption1 += alpha[alpha.index(letter2) -5 + 26]
     #   print("less than 0")
    else:
        decryption1 += alpha[alpha.index(letter2) - 5]
      #  print("greater than 0")
print(decryption1)
'''

#encryption type 3
getMessage = input("entre the messge: ").lower()
encrypted2 = ""
for letter2 in getMessage:
    if letter2 == " ":
        encrypted2 += " "
    elif ord(letter2) + 5 > ord("Z"):
        #ord returns the unicode code point for a  one character string
        encrypted2 += chr(ord(letter2) + 5 - 25)
        #Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff
    else:
        encrypted2 += chr(ord(letter2) + 5 )

print('Your encryption tex is:',encrypted2)

#decryption
EncryptedText3 = encrypted2
decryption2 = ""
for letter3 in EncryptedText3:
    if letter3 == " ":
        decryption2 += " "
    elif ord(letter2) - 5 < ord("A") or ord("a"):
        decryption2 += chr(ord(letter3) -5 + 25)
     #   print(decryption2)
    else:
        decryption2 += chr(ord(letter3) -5 )
     #   print(decryption2)
print("your decrypted text is:",decryption2)

