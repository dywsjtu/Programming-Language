PYTHON := python3

all: phase0 phase1 phase2 phase3

phase0:
	$(PYTHON) -m doctest scheme_reader.py

phase1: $(patsubst %.scm,%.test,$(wildcard phase1*tests.scm))

phase2: $(patsubst %.scm,%.test,$(wildcard phase2*tests.scm))

phase3: $(patsubst %.scm,%.test,$(wildcard phase3*tests.scm))

phase4: $(patsubst %.scm,%.test,$(wildcard phase4*tests.scm))

phase2_%: phase2_%_tests.test
	@: # null command

%.test:
	$(PYTHON) scheme_test.py $(@:.test=.scm)
