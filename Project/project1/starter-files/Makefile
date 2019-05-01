PYTHON := python3 # Python 3 executable
PAGERANK_TESTS := $(wildcard *pagerank.expected)

all: graph pagerank graph_test pagerank-tests

graph:
	python3 graph.py

pagerank:
	python3 -m doctest pagerank.py

graph_test:
	python3 graph_test.py > graph_test.out
	diff -q graph_test.out graph_test.expected

pagerank-tests: $(PAGERANK_TESTS:%.expected=%.test)

%.test:
	python3 pagerank.py $(@:pagerank.test=nodes.csv) $(@:pagerank.test=edges.csv) > $(@:.test=.out)
	diff -q $(@:.test=.out) $(@:.test=.expected)

clean:
	rm -f *.out
