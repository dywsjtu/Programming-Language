(let* ((yin
        ((lambda (cc) (display "@") cc) (call/cc (lambda (c) c))))
       (yang
        ((lambda (cc) (display "*") cc) (call/cc (lambda (c) c)))))
  (yin yang))
