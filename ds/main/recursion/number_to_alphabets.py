alpha = 'abcdefghijklmnopqrstuvwxyz'
mapping = {str(k):v for k,v in zip(range(1,27), alpha)}


def m(c):
    return mapping.get(c, None)


def interpret(s):
    if not s: return ['']

    if len(s) == 1: return [m(s)]

    c = m(s[0])
    rest = interpret(s[1:])
    comb1 = [c + substr for substr in rest]

    c = m(s[:2])
    if c:
        rest = interpret(s[2:])
        comb2 = [c + substr for substr in rest]
        comb1.extend(comb2)

    return comb1
