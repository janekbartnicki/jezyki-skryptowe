def get_number():
    file = open('./danezadanie.txt', 'r')
    return int(file.read())


def write_output(num_dec, num_hex, num_oct):
    file = open('./liczbykonwertowane.txt', 'w')
    for num in [num_dec, num_hex, num_oct]:
        file.write(str(num) + '\n')


dec_number = get_number()
write_output(dec_number, hex(dec_number), oct(dec_number))
