#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """Function determines the data set represents a valid UTF-8
       encoding
         - data [Int]: List of integers
    """
    mask_byte_1 = 1 << 7
    mask_byte_2 = 1 << 6

    byte_num = 0

    for byte in data:
        byte = byte & 255

        if byte_num == 0:
            if (byte & mask_byte_1) == 0:
                continue
            elif (byte &
                    (mask_byte_1 | mask_byte_2)) == mask_byte_1:
                return False
            elif (byte &
                    mask_byte_1 | mask_byte_2) == (mask_byte_1 | mask_byte_2):
                byte_num = 1
            elif (byte &
                    (mask_byte_1 | (1 << 5))) == (
                        mask_byte_1 | mask_byte_2 | (1 << 5)):
                byte_num = 2
            elif (byte &
                    (mask_byte_1 | (1 << 5) |
                        (1 << 4))) == (mask_byte_1 | (1 << 5) | (1 << 4)):
                byte_num = 3
            else:
                return False
        else:
            if not (byte & mask_byte_1 and not (byte & mask_byte_2)):
                return False
            byte_num -= 1

    return byte_num == 0
