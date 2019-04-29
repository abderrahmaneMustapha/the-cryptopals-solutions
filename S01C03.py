

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
english_letter_freq = {'e': 12.70, 't': 9.06, 'a': 8.17,
  'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99,
  'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
  'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29,
  'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15, 'q': 0.10, 'z': 0.07, ' ': 0.1}

def calculate_text_score(text):
    lower_case_text = text.lower()
    score = 0
    for char in lower_case_text:
        if char in english_letter_freq :
            score+= english_letter_freq[char]
        else:
            score += 0
    return score
def calculate_result(text,result_list):
    for i in range(256):
        result = xor_text(text,i)
        if len(result) % 2 == 0:
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
