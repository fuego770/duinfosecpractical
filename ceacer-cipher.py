def ceasercypher(text, shift): 
    result = ""
    for i in text:
        if (i.isupper()):
            result += chr((ord(i)+ shift - ord('A'))%26 + ord('A'))
            
        else:
            result += chr((ord(i)+ shift -ord('a'))%26 + ord('a'))
                
    return result
                
text = 'Hello'
shift = 2
result = ceasercypher(text, shift)
print(result)
