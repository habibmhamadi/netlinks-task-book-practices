import re 

def strip(st,pattern=None):
    """Removing white spaces from beginning and end of a string with regex  

    Args:
        st (String): The string to remove spaces from it.
        pattern (String): if passed, will remove the passed string from st.

    Returns:
        String
    """
    if pattern:
        left = re.compile(r'[^'+pattern+r'].*')
        right = re.compile(r'.*[^'+pattern+r'd]')
        return right.search(left.search(st).group()).group()
    left = re.compile(r'\S.*')
    right = re.compile(r'.*\S')
    return right.search(left.search(st).group()).group()

# print(strip('   Hello world!   '))

# print(strip('****Hello world!****','*'))