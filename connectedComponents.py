def connectedComponents(n, edges):
    # initializatin
    # arr contains all nodes where each node is it own parent
    arr = [i for i in range(n)]

    for edge in edges:
        union(edge, arr)

    parents = set()
    for node in arr:
        parents.add(find(node, arr))
    return len(parents)


def find(node, arr):
    """
    Returns the parent of a node
    arr: i is node and arr[i] is parent
    """
    if arr[node] != node:
        arr[node] = find(arr[node], arr)
    return arr[node]


def union(edge, arr):
    """
    connect two nodes indicated by edges
    edges == [node1,node2]
    """
    parent1 = find(edge[0], arr)
    parent2 = find(edge[1], arr)
    arr[parent1] = parent2
