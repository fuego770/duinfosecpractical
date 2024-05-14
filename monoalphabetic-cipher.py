from random import randrange

def monoalphabeticcipher(text):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    passkey = result = ''
    i=0
    
    while(len(passkey) != 26):
        shift = randrange(26)
        letter = (i+shift) % 26
    
        while (alphabet[letter] not in passkey):
            passkey += alphabet[letter]
    
        i+=1
    
    for i in text:
        result += passkey[ord(i.lower()) % 26]
        
    fresult = [result, passkey]
        
    return fresult
    
text = 'Hello'
fresult = monoalphabeticcipher(text)
print(fresult)
