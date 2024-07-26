#!/usr/bin/python3


"""
Project details:

Write a method that determines if a given data set represents a valid UTF-8
encoding.

A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
rules:

    - Prototype: def validUTF8(data)
    - Return: True if data is a valid UTF-8 encoding, else return False
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you only need to handle
    the 8 least significant bits of each integer
"""


def validUTF8(data) -> bool:
    """
    Method that determines if a given data set represents a valid UTF-8
    encoding.

    Args:
        - data: list of integers

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False
    """
    bytes = 0
    for byte in data:
        byte = byte & 255
        if bytes:
            if byte >> 6 != 2:
                return False
            bytes -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 6:
                bytes = 1
            elif byte >> 4 == 14:
                bytes = 2
            elif byte >> 3 == 30:
                bytes = 3
            else:
                return False
    return bytes == 0
