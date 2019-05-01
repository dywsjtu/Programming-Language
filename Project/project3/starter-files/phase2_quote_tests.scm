;;; Test cases for Scheme quote special form, Phase 2.

;;; *** Add more of your own here! ***

(quote x)
; expect x

'()
; expect ()

'(quote x)
; expect (quote x)

'(+ 1 3)
; expect (+ 1 3)

''x
; expect (quote x)
