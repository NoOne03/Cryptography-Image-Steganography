from stegano import lsb
from PIL import Image
def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key))

def cipherText(string, key): 
	cipher_text = [] 
	for i in range(len(string)): 
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A') 
		cipher_text.append(chr(x)) 
	return("" . join(cipher_text))

def originalText(cipher_text, key): 
	orig_text = [] 
	for i in range(len(cipher_text)): 
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A') 
		orig_text.append(chr(x)) 
	return orig_text

def encode():
	string = input("Enter data to hide: ")
	keyword = input("Enter keywrd: ")
	key = generateKey(string, keyword) 
	cipher_text = cipherText(string,key)
	print("Encoded String: ",cipher_text)
	img = input("Enter image name(with extension): ")
	new_img = input("Enter the name of the new image(with extension): ")
	if(len(cipher_text)==0):
		raise ValueError('Data is empty')
	secret = lsb.hide(img,cipher_text)
	secret.save(new_img)
	return key
def decode():
    img = input("Enter the name of secret file(with extension): ")
    cipher_text = lsb.reveal(img)
    keyword = input("Enter keyword: ")
    key = generateKey(cipher_text, keyword)
    message = originalText(cipher_text, key)
    return str(message)
    

def main(): 
    a = int(input(":: Welcome ::\n"
                        "1. Encode\n 2. Decode\n")) 
    if (a == 1): 
        encode()
    elif (a == 2): 
        print("Decoded word- " + decode()) 
    else: 
        raise Exception("Enter correct input") 
           
if __name__ == '__main__' : 
      
    # Calling main function 
    main() 
