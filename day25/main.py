from helper import *

def part1(filename: str) -> int:
    input = read_input(filename)
    graph = create_graph(input)
    edge_cut = find_edges_to_remove(graph)
    subgraphs = create_subgraphs(graph, edge_cut)
    assert len(subgraphs) == 2
    product = 1
    for subgraph in subgraphs:
        product *= len(subgraph)
    return product

if __name__ == "__main__":
    print(part1("testing"))
