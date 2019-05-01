;;; Test cases for begin special form, Phase 2.

;;; *** Add more of your own here! ***

(begin 
    (+ 1 2)
)
; expect 3

(begin 
    (+ 3 4)
    (+ 1 2)
)
; expect 3

(begin 
    (display (+ 3 4))
    (newline)
    (display (+ 1 2))
    (newline)
)
; expect 7 ; 3 ; okay
