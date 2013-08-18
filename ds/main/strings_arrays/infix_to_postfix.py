from data_structures.stacks import Stack

precedence = {'(': 0, '-': 1, '+': 1, '/': 2, '*': 2, '^': 3}
operators  = [k for k in precedence.keys() if k != '(']

def infix_to_postfix(s):
    if not s:
        raise ValueError('input cannot be None or empty string')

    seq = s.split()
    out = []
    st = Stack()

    for c in seq:
        if c in operators:
            while not st.is_empty() and precedence[c] <= precedence[st.peek()]:
                out.append(st.pop())
            st.push(c)

        elif c == '(':
            st.push(c)

        elif c == ')':
            while not st.is_empty():
                item = st.pop()
                if item == '(': break
                else: out.append(item)

        else:
            out.append(c)

    while not st.is_empty():
        out.append(st.pop())

    return ' '.join(out)
        

def eval_postfix(s):
    if not s:
        raise ValueError('input cannot be None of empty string')

    seq = s.split()
    st = Stack()

    for c in seq:
        if c not in operators:
            print 'pushing', c
            st.push(c)
        else:
            op2 = st.pop()
            op1 = st.pop()

            result = evaluate(op1, op2, c)
            st.push(result)

    return st.pop()


def evaluate(op1, op2, operator):
    expr = '{0} {1} {2}'.format(op1, operator, op2)
    return eval(expr)
