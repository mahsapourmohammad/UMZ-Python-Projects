from heapq import heappush, heappop
from collections import Counter, namedtuple
from itertools import count

# Node structure
Node = namedtuple("Node", ["char", "freq", "left", "right"])

def build_huffman_tree(text):
    freq = Counter(text)
    heap = []
    unique_counter = count() 
    
    for char, f in freq.items():
        heappush(heap, (f, next(unique_counter), Node(char, f, None, None)))
    
    while len(heap) > 1:
        f1, _, n1 = heappop(heap)
        f2, _, n2 = heappop(heap)
        merged = Node(None, f1+f2, n1, n2)
        heappush(heap, (f1+f2, next(unique_counter), merged))
    
    return heappop(heap)[2]

def build_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix+"0", codebook)
        build_codes(node.right, prefix+"1", codebook)
    return codebook

def encode_huffman(text):
    if text == "":
        return "", 0, {}
    tree = build_huffman_tree(text)
    codes = build_codes(tree)
    encoded = "".join(codes[c] for c in text)
    size_bits = len(encoded)
    return encoded, size_bits, codes

def decode_huffman(encoded, codes):
    if encoded == "" or not codes:
        return ""
    reverse_codes = {v: k for k, v in codes.items()}
    decoded = ""
    temp = ""
    for bit in encoded:
        temp += bit
        if temp in reverse_codes:
            decoded += reverse_codes[temp]
            temp = ""
    return decoded