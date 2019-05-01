;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Q5: reduce-left

; reduce-left tests: call (reduce-left-tests <reducer function>)
(define (reduce-left-tests reducer)
  (reduce-left-tester reducer - '(1 2 3 4) -8)
  (reduce-left-tester reducer expt '(2 3 2) 64)
)

(define (reduce-left-tester reducer fn items expected)
  (let ((result (reducer fn items)))
    (display "reduce-left function returned ")
    (write result)
    (display ", expected ")
    (write expected)
    (newline)
  )
)

; reduce-left solution
(define (reduce-left fn items)
  (reduce-left-helper fn (car items) (cdr items))
)

(define (reduce-left-helper fn total items)
  (if (null? items)
      total
      (reduce-left-helper fn (fn total (car items)) (cdr items))
  )
)

; reduce-left alternate solution
(define (reduce-left2 fn items)
  (if (null? (cdr items))
      (car items)
      (reduce-left2 fn (cons (fn (car items) (cadr items))
                             (cddr items)))
  )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Q3d: parser

; Call parse-test to test parsing a line. You may need to end input
; with an extra enter, if you are running this interactively.
(define (parse-test)
  (let ((next-char (peek-char)))
    (cond ((char-whitespace? next-char)
           (read-char)
           (parse-test))
          (else (let ((result (parse)))
                  (clear-line) ; clear rest of line
                  result
                )
          )
    )
  )
)

(define (parse)
  (list->string (parse-A))
)

(define (parse-A)
  (let ((next-char (peek-char)))
    (cond ((char=? next-char #\a)
           (read-char)
           (cons #\a (parse-A)))
          (else (parse-B))
    )
  )
)

(define (parse-B)
  (let ((first-char (read-char)))
    (if (char=? first-char #\b)
        (cons #\b (parse-C))
        (error "illegal character")
    )
  )
)

(define (parse-C)
  (let ((next-char (peek-char)))
    (cond ((char=? next-char #\c)
           (read-char)
           (cons #\c (parse-C)))
          (else (clear-line) '())
    )
  )
)

; Remove all characters from standard input up to and including the
; next newline.
(define (clear-line)
  (let ((next-char (read-char)))
    (if (not (or (eof-object? next-char) (char=? next-char #\newline)))
        (clear-line))))

; Abort lexing or parsing and print out the given error message.
(define (error message)
  (error-cont message))

(define error-continuation
  (let ((message (call-with-current-continuation (lambda (c) c))))
    (if (string? message)
        (begin (display "Error: ")
               (display message)
               (newline)
               (clear-line)))
    message))

(define error-cont error-continuation)
