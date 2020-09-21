import re

def is_password_strong(pwd):
    """Strong password detector using regular expression

    Args:
        pwd (String): password passed to function

    Returns:
        True: if pwd contains lowercase+upperscase+numbers and at least 8 chars
    """
    low = re.compile(r'.*[a-z].*')
    no = re.compile(r'.*[0-9].*')
    up = re.compile(r'.*[A-Z].*')
    if len(pwd)<8:
        print('password must be at least 8 characters')
        return False
    if low.match(pwd) is None:
        print('password must contains lowercase characters')
        return False  
    if no.match(pwd) is None:
        print('password must contains numbers')
        return False
    if up.match(pwd) is None:
        print('password must contains uppercase characters')
        return False
    return True
    
# print(is_password_strong('1234a1234'))