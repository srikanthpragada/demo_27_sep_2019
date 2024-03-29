def contains_upper(s):
    """
    Returns true if given string contains uppercase letter
    Args:
        s : string
    Returns:
        boolean : true if string contains upper otherwise false
    """
    for c in s:
        if c.isupper():
            return True

    return False


def contains_digit(s):
    for c in s:
        if c.isdigit():
            return True

    return False


# exclude code when imported
if __name__ == '__main__':
    print(__name__)
    print("In str_funs module!")
