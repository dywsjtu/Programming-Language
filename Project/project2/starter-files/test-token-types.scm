; Tests reading specific token types. Input format is a token type
; on its own line, followed by the token itself on the next line.
; Reads tokens until EOF is reached. Prints each read token to
; standard output.
; Example:
;   string
;   "hello world"
;   character
;   #\a
; Result:
;  (string "hello world")
;  (character #\a)

(load "lexer.scm")

(define (test-token-types)
  (let ((type (read)))
    (cond ((equal? type 'boolean) (test-token read-boolean))
          ((equal? type 'character) (test-token read-character))
          ((equal? type 'identifier) (test-token read-identifier))
          ((equal? type 'number) (test-token read-number))
          ((equal? type 'punctuator) (test-token read-punctuator))
          ((equal? type 'string) (test-token read-string)))))

(define (test-token read-fn)
  (clear-line)
  (write (read-fn))
  (newline)
  (test-token-types))

(test-token-types)
