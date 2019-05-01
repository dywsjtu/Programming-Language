"""
graph.py

ADT definitions for directed and undirected graphs.
"""

# add whatever imports you need here

class GraphException(Exception):
    """This class is used for raising exceptions in the graph ADTs.

    >>> e = GraphException()
    >>> str(e)
    ''
    >>> f = GraphException('some message')
    >>> str(f)
    'some message'
    >>> repr(e)
    "GraphException('')"
    >>> f # interpreter does the same thing as print(repr(f))
    GraphException('some message')
    """
    def __init__(self, msg=''):
        """Initializes this exception with the given message
        (defaulted to an empty string)."""
        pass # add your code here

    def __str__(self):
        """Returns the message that was passed to the constructor for
        this exception."""
        pass # add your code here

    def __repr__(self):
        """Returns the canonical string representation of this
        object."""
        return 'GraphException({})'.format(repr(str(self)))

class Node:
    """Represents a node in a graph.

    >>> n = Node('node1', weight=80, age=90)
    >>> n.identifier()
    'node1'
    >>> d = n.attributes()
    >>> d['age']
    90
    >>> d['weight']
    80
    >>> str(n)
    'Node [node1]\\n    age : 90\\n    weight : 80\\n'
    """
    def __init__(self, id, **kwargs):
        """Initializes this node with the given id. The keyword
        arguments are optional node attributes."""
        pass # add your code here

    def identifier(self):
        """Returns the identifier of this node."""
        pass # add your code here

    def attributes(self):
        """Returns a dictionary containing a copy of this node's
        attributes."""
        pass # add your code here

    def __str__(self):
        """Returns a string representation of this node, along with
        its attributes in sorted, increasing, lexicographic order."""
        pass # add your code here

class Edge:
    """Represents a directed edge in a graph.

    >>> n1, n2 = Node('node1'), Node('node2')
    >>> e = Edge(n1, n2, weight=3, color='blue')
    >>> d = e.attributes()
    >>> d['color']
    'blue'
    >>> d['weight']
    3
    >>> e.nodes() == (n1, n2)
    True
    >>> str(e)
    'Edge from node [node1] to node [node2]\\n    color : blue\\n    weight : 3\\n'
    """
    def __init__(self, u, v, **kwargs):
        """Initializes this edge with the Nodes u and v. The keyword
        arguments are optional edge attributes."""
        pass # add your code here

    def attributes(self):
        """Returns a dictionary containing a copy of this edge's
        attributes."""
        pass # add your code here

    def nodes(self):
        """Returns a tuple of the Nodes corresponding to this edge, in
        the same order as passed to the constructor."""
        pass # add your code here

    def __str__(self):
        """Returns a string representation of this edge, along with
        its attributes in sorted, increasing, lexicographic order."""
        pass # add your code here

class BaseGraph:
    """Represents a graph where the nodes and edges have optional
    attributes. This class should not be instantiated directly by a
    user.

    >>> g = BaseGraph()
    >>> len(g)
    0
    >>> g.add_node(1, a=1, b=2)
    >>> g.add_node(3, f=6, e=5)
    >>> g.add_node(2, c=3)
    >>> g.add_edge(1, 2, g=7)
    >>> g.add_edge(3, 2, h=8)
    >>> len(g)
    3
    >>> str(g.node(2))
    'Node [2]\\n    c : 3\\n'
    >>> g.node(4)
    Traceback (most recent call last):
        ...
    GraphException: ...
    >>> str(g.edge(1, 2))
    'Edge from node [1] to node [2]\\n    g : 7\\n'
    >>> g.edge(1, 3)
    Traceback (most recent call last):
        ...
    GraphException: ...
    >>> len(g.nodes())
    3
    >>> g.nodes()[0].identifier()
    1
    >>> len(g.edges())
    2
    >>> str(g.edges()[1])
    'Edge from node [3] to node [2]\\n    h : 8\\n'
    >>> 1 in g
    True
    >>> 4 in g
    False
    >>> (1, 2) in g
    True
    >>> (2, 3) in g
    False
    >>> g[1].identifier()
    1
    >>> g[(1, 2)].nodes()[0].identifier()
    1
    >>> print(g)
    BaseGraph:
    Node [1]
        a : 1
        b : 2
    Node [2]
        c : 3
    Node [3]
        e : 5
        f : 6
    Edge from node [1] to node [2]
        g : 7
    Edge from node [3] to node [2]
        h : 8
    <BLANKLINE>
    """

    def __init__(self):
        """Initializes this graph object."""
        pass # add your code here

    def __len__(self):
        """Returns the number of nodes in the graph."""
        pass # add your code here

    def add_node(self, u, **kwargs):
        """Adds a node to this graph. Requires that u, the unique
        identifier for the node, is hashable and comparable to all
        identifiers for nodes currently in the graph. The keyword
        arguments are optional node attributes. Raises a
        GraphException if a node already exists with the given ID.
        """
        pass # add your code here

    def node(self, u):
        """Returns a Node object representing the node whose ID is u.
        Raises a GraphException if the node ID is not in the graph."""
        pass # add your code here

    def nodes(self):
        """Returns a list of all the Nodes in this graph, sorted by
        increasing node IDs."""
        pass # add your code here

    def add_edge(self, u, v, **kwargs):
        """Adds an edge between the nodes whose IDs are u and v. The
        keyword arguments are optional edge attributes. Raises a
        GraphException if either node is not found, or if the graph
        already contains an edge between u and v."""
        pass # add your code here

    def edge(self, u, v):
        """Returns an Edge object representing the edge between the
        nodes with IDs u and v. Raises a GraphException if the edge is
        not in the graph."""
        pass # add your code here

    def edges(self):
        """Returns a list of all edges, each given as a (u, v) pair,
        in sorted, increasing, lexicographic order."""
        pass # add your code here

    def __getitem__(self, key):
        """If key is a node ID, returns the Node object whose ID is
        key. If key is a pair of node IDs, returns the Edge object
        corresponding to the edge between the two nodes. Raises a
        GraphException if the node IDs or edge are not in the
        graph."""
        pass # add your code here

    def __contains__(self, item):
        """If item is a node ID, returns True if there is a node in
        this graph with ID item. If item is a pair of node IDs,
        returns True if there is an edge corresponding to the two
        nodes. Otherwise, returns False."""
        pass # add your code here

    def __str__(self):
        """Returns the graph represented as a string for each
        node/edge in sorted, increasing order."""
        result = '{}:\n'.format(type(self).__name__)
        for u in self.nodes():
            result += str(u)
        for edge in self.edges():
            result += str(edge)
        return result

class UndirectedGraph(BaseGraph):
    """Represents an undirected graph where the nodes and edges have
    optional attributes.

    >>> g = UndirectedGraph()
    >>> g.add_node(1, a=1)
    >>> g.add_node(2, b=2)
    >>> g.add_edge(1, 2, c=3)
    >>> len(g)
    2
    >>> g.degree(1)
    1
    >>> g.degree(2)
    1
    >>> g.edge(1, 2).nodes() == (g.node(1), g.node(2))
    True
    >>> g.edge(2, 1).nodes() == (g.node(2), g.node(1))
    True
    >>> 1 in g
    True
    >>> 4 in g
    False
    >>> (1, 2) in g
    True
    >>> (2, 1) in g
    True
    >>> (2, 3) in g
    False
    >>> g[1].identifier()
    1
    >>> g[(1, 2)].nodes()[0].identifier()
    1
    >>> print(g)
    UndirectedGraph:
    Node [1]
        a : 1
    Node [2]
        b : 2
    Edge from node [1] to node [2]
        c : 3
    Edge from node [2] to node [1]
        c : 3
    <BLANKLINE>
    """

    def __init__(self):
        """Initializes this UndirectedGraph object."""
        pass # add your code here

    def degree(self, u):
        """Returns the degree of the node whose ID is u. Raises a
        GraphException if u is not found."""
        pass # add your code here

    # Add whatever overridden or new methods you need here

class DirectedGraph(BaseGraph):
    """Represents a directed graph where the nodes and edges have
    optional attributes.

    >>> g = DirectedGraph()
    >>> g.add_node(1, a=1)
    >>> g.add_node(2, b=2)
    >>> g.add_edge(1, 2, c=3)
    >>> len(g)
    2
    >>> g.in_degree(1)
    0
    >>> g.out_degree(1)
    1
    >>> g.in_degree(2)
    1
    >>> g.out_degree(2)
    0
    >>> g.edge(1, 2).nodes() == (g.node(1), g.node(2))
    True
    >>> g.edge(2, 1)
    Traceback (most recent call last):
        ...
    GraphException: ...
    >>> 1 in g
    True
    >>> 4 in g
    False
    >>> (1, 2) in g
    True
    >>> (2, 1) in g
    False
    >>> g[1].identifier()
    1
    >>> g[(1, 2)].nodes()[0].identifier()
    1
    >>> print(g)
    DirectedGraph:
    Node [1]
        a : 1
    Node [2]
        b : 2
    Edge from node [1] to node [2]
        c : 3
    <BLANKLINE>
    """

    def __init__(self):
        """Initializes this DirectedGraph object."""
        pass # add your code here

    def in_degree(self, u):
        """Returns the in-degree of the node whose ID is u. Raises a
        GraphException if u is not found."""
        pass # add your code here

    def out_degree(self, u):
        """Returns the out-degree of the node whose ID is u. Raises a
        GraphException if u is not found."""
        pass # add your code here

    # Add whatever overridden or new methods you need here

def read_graph_from_csv(node_file, edge_file, directed=False):
    """Reads a graph from CSV node/edge files in the format enumerated
    in the spec."""
    import csv
    result = DirectedGraph() if directed else UndirectedGraph()
    for i, filename in enumerate((node_file, edge_file)):
        attr_start = i + 1
        add_fn = result.add_node if i == 0 else result.add_edge
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)
            attr_names = header[attr_start:]
            lines = [row for row in reader]

            for line in lines:
                id, attr_values = line[:attr_start], line[attr_start:]
                attrs = {attr_names[i] : attr_values[i]
                         for i in range(len(attr_names))}
                add_fn(*id, **attrs)
    return result

def _test():
    """Run this module's doctests."""
    import doctest
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)

if __name__ == "__main__":
    # Run the doctests
    _test()
