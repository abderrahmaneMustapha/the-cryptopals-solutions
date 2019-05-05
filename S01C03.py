

def str_to_hex(str):
    return int(str , base=16)

def xor_text(text, key):
    i=0
    result= ""
    while i < len(text):
        result += hex(str_to_hex(text[i:i+2]) ^  str_to_hex(hex(key)[2:]))[2:]
        i+=2
    return result

 # english_letter_freq from http://en.wikipedia.org/wiki/Letter_frequency
english_letter_freq = {    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182}

def calculate_text_score(text):
    lower_case_text = text.lower()
    score = 0
    for char in lower_case_text:
        if char in english_letter_freq :
            score+= english_letter_freq[char]

    return score
def calculate_result(text,result_list):
    for i in range(256):
        result = xor_text(text,i)
        if len(result) % 2 != 0:
            result+="0"

        result_list.append(result)



text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
def main(text):
    result_list = []
    calculate_result(text, result_list)

    #convert hex to text
    import codecs
    decode_hex = codecs.getdecoder("hex_codec")
    score = 0
    score = max([calculate_text_score(decode_hex(result)[0]) for result in result_list])
    for result in result_list:

         if calculate_text_score(decode_hex(result)[0]) == score:

            return decode_hex(result)[0]
