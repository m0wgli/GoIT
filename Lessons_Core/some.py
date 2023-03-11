def is_equal_string(utf8_string, utf16_string):
    if utf8_string.casefold() == utf16_string.casefold():
        return True
    else:
        return False
