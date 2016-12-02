class Graph(object):

    def __init__(self, g_dict=None):
        if g_dict == None:
            g_dict = {}
        self.__g_dict = g_dict

    def verts(self):
        return list(self.__g_dict.keys())

    def edges(self):
        return self.__create_edges()

    def add_nd(self, nd):
        if nd not in self.__g_dict:
            self.__g_dict[nd] = []

    def add_edge(self, edge):
        edge = set(edge)
        (nd1, nd2) = tuple(edge)
        if nd1 in self.__g_dict:
            self.__g_dict[nd1].append(nd2)
        else:
            self.__g_dict[nd1] = [nd2]

    def __create_edges(self):
        edges = []
        for nd in self.__g_dict:
            for neigh in self.__g_dict[nd]:
                if {neigh, nd} not in edges:
                    edges.append({nd, neigh})
        return edges

    def __str__(self):
        res = "verts: "
        for k in self.__g_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__create_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["c"],
        
        }


    graph = Graph(g)

    print("Verts of graph:",graph.verts())

    print("Edges of graph:",graph.edges())

    print("Lets add nd:")
    graph.add_nd("z")

    print("Verts of graph:",graph.verts())
 
    print("Lets add an edge:")
    graph.add_edge({"a","z"})
    
    print("verts of graph:",graph.verts())

    print("Edges of graph:",graph.edges())

