from data_structures.stacks import Stack


matches = {'(':')', '[':']', '{':'}'}


def is_balanced_simple_parantheses(s):
    if not s: return True

    stack = Stack()
    for c in s:
        if c == '(':
            stack.push(c)
        if c == ')':
            if stack.is_empty(): return False
            else: stack.pop()

    return stack.is_empty()


def is_balanced_all_parantheses(s):
    if not s: return True

    stack = Stack()
    for c in s:
        if c in '([{':
            stack.push(c)
        if c in ')]}':
            if stack.is_empty(): return False
            top = stack.pop()
            if matches[top] != c: return False

    return stack.is_empty()


def test():
    print is_balanced_all_parantheses('([]()[{}])')
    print is_balanced_all_parantheses('({a + [b]})/2')
    print is_balanced_all_parantheses(')')


if __name__ == '__main__':
    test()
