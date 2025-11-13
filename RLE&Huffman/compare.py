import rle_module
import huffman_module

st = input("Please enter your Original String: ")

# RLE
rle_encoded, rle_size = rle_module.encode_rle(st)
print("\n" + "-"*40)
print("RLE Encoded Data :", rle_encoded)
print("RLE size :", rle_size, "bits")
print("RLE Decoded Data :", rle_module.decode_rle(rle_encoded))

# Huffman
huff_encoded, huff_size, codes = huffman_module.encode_huffman(st)
print("\n" + "-"*40)
print("Huffman Encoded Data :", huff_encoded)
print("Huffman size :", huff_size, "bits")
print("Huffman Decoded Data :", huffman_module.decode_huffman(huff_encoded, codes))
print("Huffman Codes :", codes)
