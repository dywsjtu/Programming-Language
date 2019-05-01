PYTHON := python3 # Python 3 executable
JAVA := javac # Java compiler

all: hw4 array util

hw4:
	$(PYTHON) -m doctest hw4.py

array: ArrayTest.class
	java ArrayTest > ArrayTest.out
	diff -q ArrayTest.out ArrayTest.expected

util: Array.class Util.class UtilTest.class
	java -ea UtilTest

%.class: %.java
	$(JAVA) $<

clean:
	rm -f *.class *.out
