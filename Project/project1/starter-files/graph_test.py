"""
graph_test.py

Starter test file for the graph module. Add your own tests to this
file.
"""

from graph import *
from pagerank import *

def undirected_test():
    g = read_graph_from_csv('characters-nodes.csv',
                            'characters-edges.csv')
    assert g.degree('0') == 6
    assert '0' in g
    assert len(g) == 10
    assert ('0', '2') in g
    assert ('2', '0') in g
    print(', '.join(n.identifier() for n in g.nodes()))
    print(g)

def simple_directed_graph():
    g = DirectedGraph()
    g.add_node(0, airport_name='DTW')
    g.add_node(1, airport_name='AMS', country='The Netherlands')
    g.add_node(2, airport_name='ORD', city='Chicago')
    g.add_edge(0, 1, flight_time_in_hours=8)
    g.add_edge(0, 2, flight_time_in_hours=1)
    g.add_edge(1, 0, airline_name='KLM')
    return g

def directed_test():
    g = simple_directed_graph()
    assert g.in_degree(2) == 1
    assert g.out_degree(0) == 2
    print(g)

# add more test cases here

if __name__ == '__main__':
    undirected_test()
    directed_test()
    # call test cases from here
