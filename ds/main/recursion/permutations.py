
def permutations(s):
    if not s:
        return ''

    if len(s) == 1:
        return [s]

    c = s[0]
    rest_of_permutations = permutations(s[1:])

    all_permutations = []
    for substring in rest_of_permutations:
        for i in range(len(substring)+1):
            new_s = substring[:i] + c + substring[i:]
            all_permutations.append(new_s)

    return all_permutations
