shorter_than(List, Size) :-
    length(List, Length),
    Length < Size.

shorter(List1, List2) :-
    length(List2, Length2),
    shorter_than(List1, Length2).

% remove(Item, List, Result)
%   True if removing all occurrences of Item in List results in
%   Result.
remove(_, [], []).
remove(Item, [Item|Rest], Result) :-
    remove(Item, Rest, Result).
remove(Item, [First|Rest], [First|Result]) :-
    Item \= First,
    remove(Item, Rest, Result).

% remove_all(Items, List, Result)
%   True if removing all occurrences of the elements in Items from
%   List results in Result.
remove_all([], List, List).
remove_all([First|Rest], List, Result) :-
    remove(First, List, FirstRemoved),
    remove_all(Rest, FirstRemoved, Result).
