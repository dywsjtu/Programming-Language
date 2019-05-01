; Utility function for testing parsing against built-in read.

(load "parser.scm")

(define (parse-all read-fn)
  (let ((result (read-fn))
        (expected (read)))
    (if (eof-object? result)
        (begin (display "Done.") (newline))
        (begin (if (not (equal? result expected))
                   (begin (display "Unexpected result:")
                          (newline)
                          (display "  expected: ")
                          (write expected)
                          (newline)
                          (display "  got: ")
                          (write result)
                          (newline)))
               (parse-all read-fn)))))
