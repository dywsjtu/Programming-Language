% Implement the smaller predicate here

smallest([First|Rest], Smallest) :-
    smallest_helper(Rest, First, Smallest).
smallest_helper([], SmallestSoFar, SmallestSoFar).
% Implement the recursive cases of smallest_helper here

% Implement the assign predicate here

% Implement the match predicate here

% Predicate to produce a sorted list of assignments.
sorted_match(Tasks, People, SortedAssignments) :-
    match(Tasks, People, Assignments),
    sort(Assignments, SortedAssignments).

% Predicate to print out the list of assignments, as well as the sum
% total of the preference ranks.
print_all(Assignments) :- print_all_helper(Assignments, 0).
print_all_helper([], Total) :-
    nl, write("Total = "), writeln(Total).
print_all_helper([[Task, Person, Rank]|AssignmentsRest], Total) :-
    write(Task), write(": "), write(Person), write(" ("),
    write(Rank), writeln(")"), NewTotal is Total + Rank,
    print_all_helper(AssignmentsRest, NewTotal).
