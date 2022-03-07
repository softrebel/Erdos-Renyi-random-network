from igraph import *
import numpy as np
import matplotlib.pyplot as plt

def graph_statistics(self):
    print("Number of vertices:", self.vcount())
    print("Number of edges:", self.ecount())
    print("Density of the graph:", 2 * self.ecount() / (self.vcount() * (self.vcount() - 1)))
    degrees = self.degree()
    print("Average degree:", sum(degrees) / self.vcount())
    print("Maximum degree:", max(degrees))
    print("Vertex ID with the maximum degree:", degrees.index(max(degrees)))
    print("Diameter of the graph:", self.diameter())
    print("Global Clustering Coefficient of the graph:", self.transitivity_undirected())
    # print("Local Clustering Coefficient of the graph:", self.transitivity_local_undirected())
    print("Average Local Clustering Coefficient of the graph:", self.transitivity_avglocal_undirected())
    print("Average Path Length of the graph:", self.average_path_length())

Graph.graph_statistics = graph_statistics



def create_edos_renyi_random_graph(p,N):
    g = Graph.Erdos_Renyi(N,p,directed=False)
    print("in practice:")
    g.graph_statistics()
    print("in theory:")
    degrees=g.degree()
    k_mean=p*(N-1)
    print("Average Path Length of the graph:",np.log10(N)/np.log10(k_mean))
    print("Average Clustering Coefficient:", k_mean/N)
    data={x:degrees.count(x) for x in degrees}
    x=sorted(list(data.keys()))
    y=[data[i] for i in x]
    plt.plot(x,y,'b')
    plt.ylabel("Number of vertices for given degree")
    plt.xlabel("Degree")
    plt.savefig('dd.svg')
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig('log-log.svg')
    g.write_graphml("test.graphml")
    return True

if __name__ == '__main__':
    p = 0.005
    N = 1000
    import sys

    if (len(sys.argv) > 1):
        N = int(sys.argv[1])
        p = float(sys.argv[2])
    create_edos_renyi_random_graph(p,N)
