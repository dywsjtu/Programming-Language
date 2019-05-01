;;; Test cases for non-standard eval special form, Phase 2.

;;; *** Add more of your own here! ***

(eval 3)
; expect 3

(eval '(+ 1 3))
; expect 4

(eval ''x)
; expect x
