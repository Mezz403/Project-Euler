
# coding: utf-8

# # XOR Decryption
# 
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# 
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
# 
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
# 
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
# 
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

# In[42]:

from collections import OrderedDict


# In[84]:

def encrypt(message, key):
    encryptedMessage = []
    
    for i in range(0,len(message)):
        encryptedMessage.append(message[i] ^ key[i % len(key)])
        
    return list(map(chr, encryptedMessage))


# In[31]:

def freq_analysis(message):
    frequencies = {}
    
    for i in range(0, len(message)):
        frequencies[message[i]] = message.count(message[i])
    return frequencies


# In[121]:

def project_euler59():
    cipher = "C:\\Users\\Alexis\\Documents\\GitHub\\Project-Euler\\Python\\059_XOR Decryption (Current)\\p059_cipher.txt"
    cipherList = []
    password = []
    
    with open(cipher) as text:
        for line in text:
            cipherList = line.replace('\n','') 
            cipherList = line.split(',')
               
        frequencies = freq_analysis(list(map(int, cipherList)))
        frequencies = [(k,v) for v,k in sorted([(v,k) for k,v in frequencies.items()])]        
        
        decryption = encrypt(list(map(int, cipherList)),[33])
        
    return decryption


# In[122]:

project_euler59()


# In[28]:

decrypt(, ['e'])


# In[32]:

freq_analysis(['\x11','\x00','\x1f','\x15','\n','S','\x0e','\n','\x01','\x15','\x01'])


# In[119]:

for i in range(32, 127):
    print(i, 101 ^ i)


# In[ ]:



