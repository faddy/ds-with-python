# implementation of a graph
# every node in a graph is represented by a Vertex object
# each Vertex object has a dictionary where:
#    each key is a neighbour vertex id
#    the values are weight of the edges


class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.neighbours = {}

    def get_neighbours(self):
        return self.neighbours.keys()

    def add_neighbour(self, vertex, weight=1):
        '''vertex is an object'''
        if not vertex: return
        self.neighbour[vertex] = weight


class Graph(object):
    def __init__(self):
        self.graph = {}

    def add_vertex(self, key):
        if key is None: return
        vertex = self.graph.get(key, None)
        if not vertex:
            vertex = Vertex(key)
            self.graph[key] = vertex
        return vertex

    def get_vertex(self, key):
        return self.graph.get(key, None)

    def add_edge(self, f, t, cost=1):
        if f is None: raise Exception('source vertex cannot be None')
        vfrom = self.graph.get(f, None)
        vto = self.graph.get(t, None)

        if not vfrom:
            vfrom = self.add_vertex(f)

        if not vto:
            vto = self.add_vertex(t)

        vfrom.neighbours[vto] = cost

    def get_vertices(self):
        return self.graph.keys()

    def __iter__(self):
        return iter(self.graph.values())

    def __str__(self):
        s = ''
        for k,v in self.graph.iteritems():
            s = s + k + ': ' + ', '.join([x.id for x in v.get_neighbours()]) + '\n'
        return s


def test():
    g = Graph()
    g.add_vertex(5)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 3)
    return g


class GraphSimple(object):
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        return len(self.graph) == 0

    def insert(self, v1, v2):
        # insert an edge from v1 -> v2
        if not v1: raise Exception('First vertex cannot be None')

        v1_edges = self.graph.get(v1, None)
        if v1_edges is None:
            self.graph[v1] = None if v2 is None else [v2]
        else:
            self.graph[v1].append(v2)

    def path_between_nodes(self, v1, v2):
        pass

    def depth_first_search(self, value):
        pass

    def breadth_first_search(self, value):
        pass

