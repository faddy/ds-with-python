from graph_structures import Graph, Vertex


def build_graph(n):
    if n < 3: return None

    g = Graph()
    for i in range(n):
        for j in range(n):
            node_id = str(i) + str(j)
            g.add_vertex(node_id)
            legit_moves = get_legit_neighbours(n, i, j)

            for sq in legit_moves:
                g.add_edge(node_id, str(sq[0]) + str(sq[1]))

    return g


def get_legit_neighbours(n, i, j):
    moves = [(-1, 2), (-1, -2), (1, 2), (1, -2), 
             (-2, 1), (-2, -1), (2, 1), (2, -1)]
    possible_squares = [(i+x, j+y) for x,y in moves]

    legit_squares = []
    for sq in possible_squares:
        if (-1 < sq[0] < n) and (-1 < sq[1] < n):
            legit_squares.append(sq)

    return legit_squares


def find_knights_tour(n):
    if n < 3: return None

    g = build_graph(n)
    path = []
    exists = find_path(g, n*n-1, g.get_vertex('00'), path)

    if exists: return path
    else: return None
    

def find_path(g, n, node, path=[]):
    print 'node:', node.id, ' n:', n, ', path:', [x.id for x in path], ' neighbors:', [x.id for x in node.get_neighbours()]
    if not node: 
        print 'hit the end of the path'
        return False

    path.append(node)
    if n == 0: return True

    exists = False
    for nbr in node.get_neighbours():
        if nbr not in path:
            exists = find_path(g, n-1, nbr, path)
            if exists: break

    if not exists:
        path.pop()            

    return exists


g = Graph()

def pr_gr():
    for v in g.graph.values():
        print v.id, v, ': ', [(x.id, x) for x in v.get_neighbours()]

def test(n,i,j):
    #return build_graph(3)
    node_id = str(i) + str(j)
    g.add_vertex(node_id)
    legit_moves = get_legit_neighbours(n, i, j)

    for sq in legit_moves:
        g.add_edge(node_id, str(sq[0]) + str(sq[1]))



