def _shift_char(c, shift):
    if not c.isalpha():
        return c
    if c.isupper():
        base = ord('A')
    else:
        base = ord('a')
    pos = ord(c) - base
    new_pos = (pos + shift) % 26
    return chr(new_pos + base)


def encrypt_message(message, shift):
    
    if not isinstance(shift, int):
        try:
            shift = int(shift)
        except Exception:
            raise TypeError("shift must be an integer")
    shift = shift % 26
    return ''.join(_shift_char(c, shift) for c in message)


def decrypt_message(message, shift):
    
    if not isinstance(shift, int):
        try:
            shift = int(shift)
        except Exception:
            raise TypeError("shift must be an integer")
    shift = shift % 26
    return ''.join(_shift_char(c, -shift) for c in message)


if __name__ == '__main__':
    message = "THE HOUSE IS NOW FOR SALE"
    shift_value = 5

    encrypted = encrypt_message(message, shift_value)
    print("Encrypted Message:", encrypted)

    decrypted = decrypt_message(encrypted, shift_value)
    print("Decrypted Message:", decrypted)
