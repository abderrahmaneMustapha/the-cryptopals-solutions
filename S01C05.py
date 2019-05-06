from S01C01 import hex_to_base64
from S01C02 import  xor_two_string, str_to_hex
text = "Burning 'em, if you ain't quick and nimble"
key = "ICE"
def text_to_hex(text):
    result = (hex(ord(c))[2:] for c in text)
    return "".join(list(result))
def repeating_xor(text, key):
    result = ""
    for t in range(len(text)):
        key_ = key[ t % 3]
        result+= xor_two_string(text_to_hex(text[t]),text_to_hex(key_))[2:]
    return result

def main(text, key):
    result = repeating_xor(text, key)
    print(result)

    #base64_text = hex_to_base64(text)




main(text, key)
