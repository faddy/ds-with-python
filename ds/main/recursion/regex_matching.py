## abcd, abc


def is_match(regex, string):

    print regex, string

    if (not regex and string) or (not string and regex):
        return False

    #if regex ^ string:
    #    return False
 
    if not regex and not string:
        return True

    c, regex = regex[0], regex[1:]

    if regex[0] == '*':
        star = True
        regex = regex[1:]
    else:
        star = False

    if star:
        if c == string[0]:
            return is_match(regex, string) or is_match(regex, string[1:])
        else:
            return is_match(regex, string)

    else:
        if c == string[0]:
            return is_match(regex, string[1:])
        else:
            return False




def is_match_new(regex, string):

    print regex, string

#    if not string:
#        # 1. regex is empty
#        if not regex: return True
#        # 2: regex is x*
#        elif len(regex) == 2 and regex.endswith('*': return True
#
#    elif not regex:
#        # regex is exhausted but string is not
#        return False

    if not regex and not string:
        return True

    if not regex or not string:
        return False

    c = regex[0]
    next_c = regex[1] if len(regex) > 1 else ''

    if next_c == '*':
        # cases:
        # 1. don't consume the star:
        #    -  consume the first char of the string: (a*b, aab) -> (a*b, ab)
        # 2. consume the star:
        #    if first chars of regex and string match:
        #    - consume first char of string: (a*b, ab) -> (b, b)
        #    if first chars don't match:
        #    - dont consume first char of string: (a*b, b) -> (b, b) ; (a*b, cb) -> (b, cb)

        # what happens to the case of (a*ab, aab)?
        # 1. (a*ab, ab)
        # 2. - (ab, ab)
        #    - (ab, aab)

        # Don't consume the star
        if is_match_new(regex, string[1:]):
            return True

        # consume the star
        regex_wo_star = regex[2:]
        if c == string[0]:
            return is_match_new(regex_wo_star, string[1:])   # is_match_new(regex_wo_star, string) or 
        else:
            return is_match_new(regex_wo_star, string)

    else:
        # the simple case when there is no star:
        # compare the first chars of the regex. if match, consume them both, else false
        if c == string[0]:
            return is_match_new(regex[1:], string[1:])
        else:
            return False










