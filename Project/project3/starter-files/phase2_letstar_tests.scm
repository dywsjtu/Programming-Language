;;; Test cases for Scheme let* special form, Phase 2.

;;; *** Add more of your own here! ***

(let* ((x 3))
  (+ x 1)
)
; expect 4

(let* ((x (+ 1 2)) (y 4))
  (- x y)
)
; expect -1

(let* ((x 3) (y x))
  (- x y)
)
; expect 0

