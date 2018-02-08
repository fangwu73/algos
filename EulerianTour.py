from random import randint

def edge(x, y):
    '''
    create a tuple between two nodes
    :param x:
    :param y:
    :return:
    '''
    return (x, y) if x < y else (y, x)

def create_tour(nodes):
    '''
    connect the first node with the second
    second with third ... and last with first
    :param nodes: list
    :return: list of tuples
    '''
    tour = []
    l = len(nodes)
    for i in range(l):
        t = edge(nodes[i], nodes[(i+1) % l])
        tour.append(t)
    return tour

def poprandom(nodes):
    '''
    randomly pop a node from the list
    :param nodes: list
    :return: list
    '''
    x_i = randint(0, len(nodes) - 1)
    return nodes.pop(x_i)

def pickrandom(nodes):
    '''
    randomly pick one node
    :param nodes: list
    :return: int
    '''
    x_i = randint(0, len(nodes) - 1)
    return nodes[x_i]

def check_nodes(x, nodes, tour):
    '''
    check if x is connected to all nodes in nodes and all edges are in tour
    if not, connect it with a node in nodes and
    add the tuple to the list of tour and
    return the connected node
    if yes, return None
    :param x:
    :param nodes: list of int
    :param tour: list of tuple
    :return: None if all
    '''
    for i, n in enumerate(nodes):
        t = edge(x, n)
        if t not in tour:
            tour.append(t)
            nodes.pop(i)
            return n
    return None


def create_tour_rand(nodes):
    '''
    start with all unconnected
    :param nodes:
    :return: list of tuples
    '''
    connected = []
    degree = {}
    unconnected = [n for n in nodes]
    tour = []
    # pick two random unconnected nodes for an edge to start with
    x = poprandom(unconnected)
    y = poprandom(unconnected)
    connected.append(x)
    connected.append(y)
    tour.append(edge(x, y))
    degree[x] = 1
    degree[y] = 1
    # pick a random node from the unconnected list
    # and create an edge to connect it until all nodes are connected
    while len(unconnected) > 0:
        x = pickrandom(connected)
        y = poprandom(unconnected)
        connected.append(y)
        tour.append(edge(x, y))
        degree[x] += 1
        degree[y] = 1
    # make sure each node has even degree
    odd_nodes = [k for k, v in degree.items() if v % 2 == 1]
    even_nodes = [k for k, v in degree.items() if v % 2 == 0]
    # since the sum of degrees of a graph is even
    # there will always be even number of odd nodes

    # connect odd_nodes together
    while len(odd_nodes) > 0:
        x = poprandom(odd_nodes)
        cn = check_nodes(x, odd_nodes, tour)
        if cn is not None:
            even_nodes.append(x)
            even_nodes.append(cn)
        else:
            # all the odd nodes have been all connected to x
            # need to find an even node to connect to
            cn = check_nodes(x, even_nodes, tour)
            # cn cannot be None and needs to be added to odd_nodes
            odd_nodes.append(cn)
            # x is now an even node
            even_nodes.append(x)
    return tour


