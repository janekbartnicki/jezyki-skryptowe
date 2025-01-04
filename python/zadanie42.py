def shannon_fano_encode(text):
    char_probs = {char: text.count(char) / len(text) for char in set(text)}

    sorted_chars = sorted(char_probs.items(), key=lambda x: x[1], reverse=True)

    def _encode_recursive(chars, code=''):
        if len(chars) == 1:
            codes[chars[0][0]] = code
            return

        split = len(chars) // 2
        _encode_recursive(chars[:split], code + '0')
        _encode_recursive(chars[split:], code + '1')

    codes = {}
    _encode_recursive(sorted_chars)

    encoded_text = ''.join(codes[char] for char in text)

    return codes, encoded_text


def shannon_fano_decode(encoded_text, codes):
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
codes, encoded_text = shannon_fano_encode(text)
print("Kod SF:", codes)
print("Tekst zakodowany:", encoded_text)
decoded_text = shannon_fano_decode(encoded_text, codes)
print("Tekst zdekodowany:", decoded_text)