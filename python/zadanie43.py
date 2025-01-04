import heapq


def huffman_encode(text):
    char_probs = {char: text.count(char) for char in set(text)}

    heap = [[weight, [symbol, '']] for symbol, weight in char_probs.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    codes = {symbol: code for symbol, code in heap[0][1:]}

    encoded_text = ''.join(codes[char] for char in text)

    return codes, encoded_text


def huffman_decode(encoded_text, codes):
    decoded_text = []
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        for char, code in codes.items():
            if code == current_code:
                decoded_text.append(char)
                current_code = ''
                break
    return ''.join(decoded_text)


text = "JEZYKI SKRYPTOWE"
codes, encoded_text = huffman_encode(text)
print("Kod H:", codes)
print("Tekst zakodowany:", encoded_text)
decoded_text = huffman_decode(encoded_text, codes)
print("Tekst zdekodowany:", decoded_text)