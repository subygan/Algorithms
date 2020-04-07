class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):

        return list(self.__graph_dict.keys())

    def edges(self):

        edge_list = []

        for key in self.__graph_dict.keys():
            for con in self.__graph_dict[key]:
                if {con,key} not in edge_list:
                    print(con,key)
                    edge_list.append({con,key})
        return edge_list


if __name__ == "__main__":

    g = { "a": ["d"],
          "b": ["c"],
          "c": ["b", "c", "d", "e"],
          "d": ["a", "c"],
          "e": ["c"],
          "f": []
        }

    graph = Graph(g)

    print("Edges of graph:")
    print(graph.edges())