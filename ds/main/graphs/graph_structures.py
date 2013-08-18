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

    #def __str__(self):
       # return str(self.id) + ' connected to: ' + str([x.id for x in self.get_neighbours()])


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


if __name__ == '__main__':
    print test()
