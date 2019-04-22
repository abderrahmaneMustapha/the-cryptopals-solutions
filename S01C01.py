
Hex_num= "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
import binascii
def hex_to_base64():
    base = binascii.b2a_base64(Hex_num.decode('hex'))
    return base

def str_to_hex(str):
    return int(str , base=16)

def xor_two_string(str1 , str2):
    a = str_to_hex(str1)
    b = str_to_hex(str2)
    return hex(a ^ b)

str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
       #1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b373c
str2 = "5"

print(xor_two_string(str1, str2)[2:-1])
