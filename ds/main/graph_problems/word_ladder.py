import os
from data_structures.graphs import Graph
from collections import deque

def build_buckets(word_file):
    if not word_file: return None
    if not os.path.exists(word_file): return None

    buckets = {}
    with open(word_file, 'r') as f:
        for line in f:
            if len(line) == 5 and "'" not in line:
                word = line[:-1].lower()
                for i in range(len(word)):
                    bucket_id = word[:i] + '_' + word[i+1:]
                    if not buckets.get(bucket_id, None):
                        buckets[bucket_id] = set([word])
                    else:
                        buckets[bucket_id].add(word)

    return buckets


def build_graph(buckets):
    if not buckets: return None

    g = Graph()
    for key, words in buckets.iteritems():
        for word in words:
            for w in words:
                if w != word:
                    g.add_edge(w, word)

    return g


class Node(object):
    def __init__(self, i, p):
        self.id = i
        self.parent = p


def bfs_find_path(graph, fr, to):
    '''
    bfs search to find a path between 'fr' and 'to' nodes
    During traversal, when we add a node to the queue,
        we add a tuple pair of (node, node's parent tuple)
        so that we can keep track of the parent/path
        however, this is quite wasteful as it requires a lot more space
    '''
    from_v = graph.get_vertex(fr)
    if not from_v: raise Exception('Node {0} not in graph'.format(fr))

    to_v = graph.get_vertex(to)
    if not to_v: raise Exception('Node {0} not in graph'.format(to))

    queue = deque()
    visited = {}
    queue.appendleft( (from_v, None) )
    result = None

    while queue:
        curr_node = queue.pop()

        if curr_node[0] not in visited:
            if curr_node[0].id == to:
                result = curr_node
                break

            neighbours = curr_node[0].get_neighbours()
            #print curr_node[0].id + ':', [x.id for x in neighbours]
            for node in neighbours:
                n = (node, curr_node)
                queue.appendleft(n)

            visited[curr_node[0]] = True

    return result


def dfs_find_path(graph, fr, to):
    from_v = graph.get_vertex(fr)
    if not from_v: raise Exception('Node {0} not in graph'.format(fr))

    to_v = graph.get_vertex(to)
    if not to_v: raise Exception('Node {0} not in graph'.format(to))

    path = dfs(from_v, to_v)

def dfs(fr, to, path=[]):
    '''
    Since this uses recursion and our graph is fairly large,
    we run out of memory for stack allocation for our use case.
    Hence try bfs for large problem set (or iterative method)'''
    print [x.id for x in path]
    if not fr: return None
    if fr in path: return None

    newpath = path + [fr]
    neighbours = fr.get_neighbours()
    for nbr in neighbours:
        if not nbr in newpath:
            if nbr.id == to.id:
                print newpath + [nbr]
                return
            else:
                dfs(nbr, to, newpath)


def find_word_ladder(from_word, to_word):
    wordfile = '/home/fahad/dictionary.txt'
    buckets = build_buckets(wordfile)
    g = build_graph(buckets)
    rev_path = bfs_find_path(g, from_word, to_word)
    path = []
    while rev_path:
        path.append(rev_path[0].id)
        rev_path = rev_path[1]
    return list(reversed(path))

def create_dummy_graph():
    g = Graph()
    g.add_edge('bat', 'cat')
    g.add_edge('bat', 'ban')
    g.add_edge('cat', 'sat')
    g.add_edge('sat', 'bat')
    g.add_edge('sat', 'sit')
    return g

def test():
    g = create_dummy_graph()
    return bfs_find_path(g, 'bat', 'sit')

if __name__ == '__main__':
    print find_word_ladder('polo', 'pool')
