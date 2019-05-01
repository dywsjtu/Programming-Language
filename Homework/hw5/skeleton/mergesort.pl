merge([], List, List).
% write the remaining facts and rules here

mergesort([], []).
mergesort([Item], [Item]).
mergesort(List, Sorted) :- writeln(List). % add more terms before the .
