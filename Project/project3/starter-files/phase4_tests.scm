;;; Test cases for Scheme, Phase 4.

;;; *** Add more of your own here! ***

(define (y c) (c x))

(define x 3)

(define z (+ 1 (call/cc y)))
z
; expect 4

(define (a b) (+ b (call/cc y)))

(define c (call/cc (lambda (cc) cc)))

(define d c)

(d 3)
c
; expect 3

(d 4)
c
; expect 4

(d 'a)
c
; expect a

(define e (begin (display 2) (call/cc (lambda (cc) cc))))
; expect 2e

(define f e)

(f 5)
; expect e
e
; expect 5

(define (foo cc) cc)

(define bar (cons '(1 2) (call/cc foo)))
; expect bar

(define baz (cdr bar))

(baz 3)
; expect bar
bar
; expect ((1 2) . 3)
(baz '(3 4))
; expect bar
bar
; expect ((1 2) 3 4)
