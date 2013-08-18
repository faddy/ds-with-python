
def are_anagrams(s1, s2):
    if s1 is None or s2 is None:
        return False

    if not s1 and not s2:
        return True

    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True

    letters = {}
    for c in s1:
        val = letters.get(c, None)
        if not val:
            letters[c] = 1
        else:
            letters[c] = val + 1

    for c in s2:
        val = letters.get(c, None)
        if not val:
            return False
        elif val == 1:
            del(letters[c])
        else:
            letters[c] = val - 1

    return True


