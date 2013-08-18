
class Graph(object):
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


def create_test_graph():
    g = Graph()
    g.insert(1, 2)
    g.insert(1, 3)
    g.insert(3, 4)
    g.insert(3, 5)
    g.insert(3, 6)
    g.insert(4, 2)
    g.insert(5, 7)
    g.insert(6, 8)
    g.insert(6, 9)
    g.insert(6, 10)
    g.insert(6, 11)
    g.insert(8, 5)
    return g
