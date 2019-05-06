
Hex_num= "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
import binascii
def hex_to_base64(Hex_num):
    base = binascii.b2a_base64(Hex_num.decode('hex'))
    return base
