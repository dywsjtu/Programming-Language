TESTS := $(wildcard tests/*.uc)
OUTPUTS := $(patsubst %.uc,%.test,$(TESTS))
PYTHON := python3

all: test

test: $(OUTPUTS)

%.test: %.uc
	@echo "Testing $<..."
	$(PYTHON) ucc.py -S -T $< > $(patsubst %.uc,%.out,$<) || true
	$(PYTHON) ucccheck.py $<
	@echo

clean:
	rm -f tests/*.out tests/*.types
