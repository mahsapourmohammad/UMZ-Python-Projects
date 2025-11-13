def encode_rle(inp):
    if inp == "":
        return "", 0
    
    first = inp[0]
    count = 0
    encoded = []
    size_bits = 0  
    
    for i in inp:
        if i == first:
            count += 1
        else:
            
            encoded.append(str(count) + first)

            
            bits = count.bit_length()
            size_bits += bits  #number valume
            size_bits += 8     # character valume

            first = i
            count = 1
    

    encoded.append(str(count) + first)
    bits = count.bit_length()
    size_bits += bits
    size_bits += 8
    
    return ''.join(encoded), size_bits

#----------------------------------------------------------------------------
def decode_rle(inp):
    decoded = []
    if inp == '':
        return ""
    num = ''
    for i in inp:
        if i.isdigit():
            num += i
        else:
            if num != '':
                decoded.append(i * int(num))
                num = ''
    return ''.join(decoded)






inp = input('Which action do you want to do? (d) for decode, (e) for encode:')
if inp == 'd':
    st = input("Please enter your Encoded String: ")
    decoded = decode_rle(st)
    print('*'*30)
    print("RLE Decoded Data is :", decoded)
    encoded,size = encode_rle(decoded)
    print("RLE Encoded Data is :", encoded)

elif inp == 'e':
    st = input("Please enter your Decoded (Original) String: ")
    encoded,size = encode_rle(st)
    print('*'*30)
    print("RLE Encoded Data is :", encoded)
    print("RLE size :", size)
    print("RLE Decoded Data is :", decode_rle(encoded))
