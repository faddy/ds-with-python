
def is_palindrome(s):

    if s is None: return True

    if len(s) <= 1: return True

    return s[0] == s[-1] and is_palindrome(s[1:-1])
