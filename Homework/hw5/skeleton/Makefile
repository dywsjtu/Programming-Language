PROLOG := swipl -q # SWI-Prolog

all: add_to_all mergesort match

add_to_all:
	$(PROLOG) add_to_all.pl < add_to_all.in > add_to_all.out
	diff -q add_to_all.out add_to_all.correct

mergesort:
	$(PROLOG) mergesort.pl < merge.in > merge.out
	diff -q merge.out merge.correct
	$(PROLOG) mergesort.pl < sort.in > sort.out
	diff -q sort.out sort.correct

match:
	$(PROLOG) match.pl < smaller.in > smaller.out
	diff -q smaller.out smaller.correct
	$(PROLOG) match.pl < smallest1.in > smallest1.out
	diff -q smallest1.out smallest1.correct
	$(PROLOG) match.pl < smallest2.in > smallest2.out
	diff -q smallest2.out smallest2.correct
	$(PROLOG) match.pl < assign.in > assign.out
	diff -q assign.out assign.correct
	$(PROLOG) match.pl < match1.in > match1.out
	diff -q match1.out match1.correct
	$(PROLOG) match.pl < match2.in > match2.out
	diff -q match2.out match2.correct

extras:
	$(PROLOG) extras.pl < sublists.in > sublists.out
	diff -q sublists.out sublists.correct
	$(PROLOG) extras.pl < unzip.in > unzip.out
	diff -q unzip.out unzip.correct
	$(PROLOG) extras.pl < numbers.in > numbers.out
	diff -q numbers.out numbers.correct

clean:
	rm -f *.out
