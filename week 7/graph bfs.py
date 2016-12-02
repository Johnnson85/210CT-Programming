class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_node(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list"""
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph_dict:
            self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]

    def __generate_edges(self):
        edges = []
        for node in self.__graph_dict:
            for neighbour in self.__graph_dict[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    

    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False]*(len(self.__graph_dict))
 
        
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
            s = queue.pop(0)
            print (s)
 
            for i in self.__graph_dict[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["c"],
        
        }


    graph = Graph(g)

    
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Edges of graph:",graph.edges())

    print (" BFT starting form vertex b")
    graph.BFS({"b"})
