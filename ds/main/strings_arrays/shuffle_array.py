import random

def shuffle(arr, from_code=False):
    '''
    shuffles an array and returns it so that each 
    rearrangement is equally probable
    '''
    if not arr or len(arr) == 1: return arr

    #newarr = [x for x in arr]
    for i in reversed(xrange(1, len(arr))):
         random_index = int(random.random() * i+1) if from_code else random.choice(range(i))
         arr[i], arr[random_index] = arr[random_index], arr[i]

    #return arr


def test(arr, N):
    d = {}
    my_arr = [x for x in arr]
    for i in range(N):
        shuffle(my_arr)
        arrstr = ''.join([str(x) for x in my_arr])
        d[arrstr] = d.get(arrstr, 0) + 1

    e = {}
    code_arr = [y for y in arr]
    for i in range(N):
        shuffle(code_arr, from_code=True)
        arrstr = ''.join([str(x) for x in code_arr])
        e[arrstr] = e.get(arrstr, 0) + 1

    return (d, e)
        

if __name__ == '__main__':
    arr = range(1, 2)
    print arr
    print '----'
    print test(arr, 100)
