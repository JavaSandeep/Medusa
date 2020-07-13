visited=set()

def dfs(G, s):
    """
    function for dfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # append start node to visited
    visited.add(s)

    # iterating over all the neighbours of the node
    # in inspection
    for _n in G.get(s):
        # if neighbour node is not visited
        # then visit dfs it
        if _n not in visited:
            dfs(G, _n)
            # goes to depth first
            #' to add extra functionality
