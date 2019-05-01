;;; Test cases for Scheme, Phase 3.

;;; *** Add more of your own here! ***

; Tail call optimization test
(define (sum n total)
  (if (zero? n) total
    (sum (- n 1) (+ n total))))
(sum 1001 0)
; expect 501501
