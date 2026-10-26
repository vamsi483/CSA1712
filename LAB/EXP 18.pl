sum(0, 0).
sum(N, S) :-
    N > 0,
    N1 is N - 1,
    sum(N1, S1),
    S is N + S1.

:- initialization(main).
main :-
    sum(5, S),
    write(S),
    nl,
    halt.
