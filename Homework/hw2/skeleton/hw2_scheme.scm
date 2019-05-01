; write your solution here

(interleave '(1 3) '(2 4 6 8))
; expect (1 2 3 4 6 8)
(interleave '(2 4 6 8) '(1 3))
; expect (2 1 4 3 6 8)
(interleave '(1 3) '(1 3))
; expect (1 1 3 3)
