import networkx as nx

def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

def create_graph(input: list[str]) -> nx.Graph:
    graph = nx.Graph()
    for line in input:
        node, nodes = [x.strip() for x in line.split(":")]
        for n in [x.strip() for x in nodes.split(" ")]:
            graph.add_edge(node, n)
    return graph

def find_edges_to_remove(graph: nx.Graph) -> set:
    return nx.minimum_edge_cut(graph)

def create_subgraphs(graph: nx.Graph, edge_cut: set) -> list[set]:
    graph2 = graph.copy()
    graph2.remove_edges_from(edge_cut)
    return list(nx.connected_components(graph2))
