def xor_two_string(str1 , str2):
    a = str_to_hex(str1)
    b = str_to_hex(str2)
    return hex(a ^ b)

def str_to_hex(str):
    return int(str , base=16)

str1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
str2 = "5"
