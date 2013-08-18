# two pointers: 
# src: index from which the next item is copied
# dst: index into which the item is copied

# src = 0, dst = 0
# walk through the sequence.
# if item is seen: increment src
# else copy from src to dst, increment src, increment dst, add item to seen


def remove_dups(seq):
    if not seq:
        return seq

    is_string = bool(isinstance(seq, str))

    if is_string:
        seq = list(seq)

    seen = {}
    dst = 0

    for src in range(len(seq)):
       item = seq[src]
       if not seen.get(item, False):
           # item not seen yet
           seq[dst] = seq[src]
           dst += 1
           seen[item] = True

    if is_string:
        return ''.join(seq[:dst])
    else:
        return seq[:dst]
