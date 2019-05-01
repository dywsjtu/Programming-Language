CORRECT_TESTS := $(wildcard tests/*.uc)
PHASE4_TESTS := tests/default.uc tests/equality.uc tests/hello.uc tests/use_before_decl.uc
PHASE5_TESTS := $(filter-out $(PHASE4_TESTS),$(CORRECT_TESTS))
LIB_DIR := .
PYTHON := python3
CXX := g++

all: tests

tests: phase1 phase2 phase3 phase4 phase5

phase1: $(CORRECT_TESTS:.uc=.phase1)

phase2: $(CORRECT_TESTS:.uc=.phase2)

phase3: $(CORRECT_TESTS:.uc=.phase3)

phase4: PHASE = 4
phase4: $(PHASE4_TESTS:.uc=.phase45)

phase5: PHASE = 5
phase5: $(PHASE5_TESTS:.uc=.phase45)

%.phase1: %.uc
	@echo "Running Phase 1 test on $<..."
	$(PYTHON) ucc.py -C --backend-phase=1 $<
	$(CXX) --std=c++14 -I$(LIB_DIR) -c -o $(<:.uc=_phase1.o) $(<:.uc=_phase1.cpp)
	@echo

%.phase2: %.uc
	@echo "Running Phase 2 test on $<..."
	$(PYTHON) ucc.py -C --backend-phase=2 $<
	$(CXX) --std=c++14 -I$(LIB_DIR) -c -o $(<:.uc=_phase2.o) $(<:.uc=_phase2.cpp)
	@echo

%.phase3: %.uc
	@echo "Running Phase 3 test on $<..."
	$(PYTHON) ucc.py -C --backend-phase=3 $<
	$(CXX) --std=c++14 -I$(LIB_DIR) -o $(<:.uc=_phase3.exe) $(<:.uc=_phase3.cpp)
	$(<:.uc=_phase3.exe)
	@echo

%.phase45: %.uc
	@echo "Running Phase $(PHASE) test on $<..."
	$(PYTHON) ucc.py -C $<
	$(CXX) --std=c++14 -I$(LIB_DIR) -o $(<:.uc=.exe) $(<:.uc=.cpp)
	$(<:.uc=.exe) 20 10 5 2 > $(<:.uc=.run)
	diff -q $(<:.uc=.run.correct) $(<:.uc=.run)
	@echo

life: life.uc
	@echo "Testing life.uc..."
	$(PYTHON) ucc.py -C life.uc
	$(CXX) --std=c++14 -I$(LIB_DIR) -o life.exe life.cpp
	./life.exe | diff -q - life_test.correct
	@echo

clean:
	rm -f $(CORRECT_TESTS:.uc=.cpp) tests/*.o tests/*.exe tests/*.run life.cpp life.exe
