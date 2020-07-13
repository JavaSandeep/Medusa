from collections import deque

def bfs(G, s):
    """
    function for bfs traversal of the graph
    :param: G for graph as dict
    :s: int for start node
    """
    # root node is said to have 0 depth
    # in case of tree
    depth=0

    visited=set()
    nQueue=deque()

    nQueue.append([s,depth])
    visited.add(s)

    # to iterate through whole nodes
    while len(nQueue)>0:
        # in case depth is not required
        #v,_=nQueue.popleft()
        v,r=nQueue.popleft()

        # iterating over all the neighbours of the node
        # in inspection
        for _n in G.get(v):
            # if neighbour node is not visited
            # then visit it
            if _n not in visited:
                nQueue.append([_n,r+1])
                visited.add(_n)
                #' to add extra functionality
