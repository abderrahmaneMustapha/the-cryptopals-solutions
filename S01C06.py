def hamming_distance(str1, str2):
    distance = 0
    if len(str1) == len(str2):
        #str1_bin = ''.join([bin(ord(s))[2:] for s in str1])
        #str2_bin = ''.join([bin(ord(s))[2:] for s in str2])

        for s1 , s2 in zip(str1, str2):
            temp =  ord(s1)^ ord(s2)

            distance += sum([1  for d in bin(temp) if d=='1'])
    print(distance)

hamming_distance(b'this is a test', b'wokka wokka!!!')
