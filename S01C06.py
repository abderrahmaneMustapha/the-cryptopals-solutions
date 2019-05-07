def add_zero(str):
    if len(str) < 6:
        str+='0'
    return str


def hamming_distance(str1, str2):
    distance = 0
    if len(str1) == len(str2):
        str1_bin = ''.join([add_zero(bin(ord(s))[2:]) for s in str1])
        str2_bin = ''.join([add_zero(bin(ord(s))[2:]) for s in str2])

        for s1 , s2 in zip(str1_bin, str2_bin):
            if  s1 != s2  :
                distance += 1
    print(distance)


hamming_distance('this is a test', 'wokka wokka!!!')
