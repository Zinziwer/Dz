# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
a = 'FFFAAAAAAUIMMMMMMMMMMMMMMMMMJJSSAAAA'
def encode(message):
    encoded_message = ""
    i = 0

    while i <= len(message) - 1:
        count = 1
        char = message[i]
        j = i
        while j < len(message) - 1:
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_message = encoded_message + str(count) + char
        i = j + 1
    return encoded_message

def decode(message):
    decode = ''
    count = ''
    for char in message:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
encoded_val = encode(a)
print(encoded_val)
decoded_val = decode(encoded_val)
print(decoded_val)