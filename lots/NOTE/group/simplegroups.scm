;;; Scheme program to calculate the orders of finite simple groups.

;;; This program is distributed under the terms of the GNU General
;;; Public License: you are free to redistribute it and to modify it,
;;; provided you make your modifications available under the terms of
;;; the said license if you redistribute them.  Because this program
;;; is distributed freely, there is ABSOLUTELY NO WARRANTY, express or
;;; implied.

;; Return the gcd of its arguments.
(define (gcd . terms)
  (define (gcd-2 u v)
    (define (gcd-loop u v)
      (if (= v 0)
	  u
	  (gcd-loop v (remainder u v))))
    (cond
     ((< u 0)
      (gcd-2 (- u) v))
     ((< v 0)
      (gcd-2 u (- v)))
     ((< u v)
      (gcd-2 v u))
     (else
      (gcd-loop u v))))
  (if (null? terms)
      0
      (gcd-2 (car terms)
	     (apply gcd (cdr terms)))))

;; Return n raised to the k-th power.
(define (power n k)
  (define (power-loop a n k)
    (if (= k 0)
	a
	(power-loop (* a n) n (- k 1))))
  (power-loop 1 n k))

;; Return the list of integers from a to b.
(define (interval a b)
  (if (> a b)
      '()
      `(,a . ,(interval (+ a 1) b))))

;; Exact quotient of a by b.
(define (e-quotient a b)
  (if (not (= (remainder a b) 0))
      (begin
	(map display
	     `("Alert!  The quotient of " ,a " by " ,b " is not exact!"))
	(newline)))
  (quotient a b))

;; Return n factorial.
(define (fact n)
  (define (fact-loop k n)
    (if (= n 0)
	k
	(fact-loop (* k n) (- n 1))))
  (fact-loop 1 n))

;; Determine whether p is prime.
(define (is-prime? p)
  (define (loop k)
    (if (>= k p)
	#t
	(if (= (remainder p k) 0)
	    #f
	    (loop (+ k 1)))))
  (loop 2))

;; The orders of the families of simple groups of Lie type.  See
;; M. Aschbacher, ``Finite group theory'' (Cambridge studies in
;; advanced mathematics 10), table 16.1 page 251

(define (order-an n q)
  (e-quotient (* (power q (e-quotient (* n (+ n 1)) 2))
		 (apply * (map (lambda (i) (- (power q (+ i 1)) 1))
			       (interval 1 n))))
	      (gcd (+ n 1) (- q 1))))

(define (order-bn n q)
  (e-quotient (* (power q (* n n))
		 (apply * (map (lambda (i) (- (power q (* i 2)) 1))
			       (interval 1 n))))
	      (gcd 2 (- q 1))))

(define (order-cn n q)
  (e-quotient (* (power q (* n n))
		 (apply * (map (lambda (i) (- (power q (* i 2)) 1))
			       (interval 1 n))))
	      (gcd 2 (- q 1))))

(define (order-dn n q)
  (e-quotient (* (power q (* n (- n 1)))
		 (- (power q n) 1)
		 (apply * (map (lambda (i) (- (power q (* i 2)) 1))
			       (interval 1 (- n 1)))))
	      (gcd 4 (- (power q n) 1))))

(define (order-e6 q)
  (e-quotient (* (power q 36)
		 (apply * (map (lambda (i) (- (power q i) 1))
			       '(12 9 8 6 5 2))))
	      (gcd 3 (- q 1))))

(define (order-e7 q)
  (e-quotient (* (power q 63)
		 (apply * (map (lambda (i) (- (power q i) 1))
			       '(18 14 12 10 8 6 2))))
	      (gcd 2 (- q 1))))

(define (order-e8 q)
  (* (power q 120)
     (apply * (map (lambda (i) (- (power q i) 1))
		   '(30 24 20 18 14 12 8 2)))))

(define (order-f4 q)
  (* (power q 24)
     (apply * (map (lambda (i) (- (power q i) 1))
		   '(12 8 6 2)))))

(define (order-g2 q)
  (* (power q 6)
     (- (power q 6) 1)
     (- (power q 2) 1)))

(define (order-2an n q)
  (e-quotient (* (power q (e-quotient (* n (+ n 1)) 2))
		 (apply * (map (lambda (i) (- (power q (+ i 1))
					      (power -1 (+ i 1))))
			       (interval 1 n))))
	      (gcd (+ n 1) (+ q 1))))

(define (order-2b2 q2)
  (* (power q2 2)
     (+ (power q2 2) 1)
     (- q2 1)))

(define (order-2dn n q)
  (and (>= n 2)
       (e-quotient (* (power q (* n (- n 1)))
		      (+ (power q n) 1)
		      (apply * (map (lambda (i) (- (power q (* i 2)) 1))
				    (interval 1 (- n 1)))))
		   (gcd 4 (+ (power q n) 1)))))

(define (order-3d4 q)
  (* (power q 12)
     (+ (power q 8) (power q 4) 1)
     (- (power q 6) 1)
     (- (power q 2) 1)))

(define (order-2e6 q)
  (e-quotient (* (power q 36)
		 (apply * (map (lambda (i) (- (power q i)
					      (power -1 i)))
			       '(12 9 8 6 5 2))))
	      (gcd 3 (+ q 1))))

(define (order-2f4 q2)
  (* (power q2 12)
     (+ (power q2 6) 1)
     (- (power q2 4) 1)
     (+ (power q2 3) 1)
     (- q2 1)))

(define (order-2g2 q2)
  (* (power q2 3)
     (+ (power q2 3) 1)
     (- q2 1)))

;; Call (cont tag ord) with tag describing all non-abelian finite
;; simple groups whose order ord is less than bound.
(define (spew-simplegroups bound cont)
  (define (spew-alt-loop k)
    (let ((ord (e-quotient (fact k) 2)))
      (if (< ord bound)
	  (begin
	    (cont `(alt ,k) ord)
	    (spew-alt-loop (+ k 1))))))
  (define (spew-single-loop fun tag-fun check-fun b e *f*)
    (if (is-prime? b)
	(let ((ord (fun (power b e))))
	  (if (< ord bound)
	      (begin
		(if (check-fun b e)
		    (cont (tag-fun (power b e)) ord))
		(spew-single-loop fun tag-fun check-fun
				  b (+ e 1) #t))
	      (if *f*
		  (spew-single-loop fun tag-fun check-fun
				    (+ b 1) 1 #f))))
	(spew-single-loop fun tag-fun check-fun (+ b 1) 1 #f)))
  (define (spew-double-loop fun tag-fun check-fun k b e *k* *f*)
    (if (is-prime? b)
	(let ((ord (fun k (power b e))))
	  (if (< ord bound)
	      (begin
		(if (check-fun k b e)
		    (cont (tag-fun k (power b e)) ord))
		(spew-double-loop fun tag-fun check-fun
				  k b (+ e 1) #t #t))
	      (if *f*
		  (spew-double-loop fun tag-fun check-fun
				    k (+ b 1) 1 #t #f)
		  (if *k*
		      (spew-double-loop fun tag-fun check-fun
					(+ k 1) 2 1 #f #f)))))
	(spew-double-loop fun tag-fun check-fun k (+ b 1) 1 *k* #f)))
  (define (spew-isolated tag ord)
    (if (< ord bound) (cont tag ord)))
  (spew-alt-loop 5)
  (spew-double-loop order-an
		    (lambda (l q) `(lie a ,l ,q))
		    (lambda (l b e)
		      (cond
		       ((= l 1) (not (or (and (= e 1) (<= b 5))
					 (and (= e 2) (<= b 3)))))
		       ((= l 2) (not (and (= e 1) (= b 2))))
		       ((= l 3) (not (and (= e 1) (= b 2))))
		       (else #t)))
		    1 2 1 #f #f)
  (spew-double-loop order-bn
		    (lambda (l q) `(lie b ,l ,q))
		    (lambda (l b e)
		      (not (= b 2)))
		    2 2 1 #f #f)
  (spew-double-loop order-cn
		    (lambda (l q) `(lie c ,l ,q))
		    (lambda (l b e)
		      (if (= l 2)
			  (and (= b 2) (>= e 2))
			  #t))
		    2 2 1 #f #f)
  (spew-double-loop order-dn
		    (lambda (l q) `(lie d ,l ,q))
		    (lambda (l b e) #t)
		    4 2 1 #f #f)
  (spew-single-loop order-e6
		    (lambda (q) `(lie e 6 ,q))
		    (lambda (b e) #t)
		    2 1 #f)
  (spew-single-loop order-e7
		    (lambda (q) `(lie e 7 ,q))
		    (lambda (b e) #t)
		    2 1 #f)
  (spew-single-loop order-e8
		    (lambda (q) `(lie e 8 ,q))
		    (lambda (b e) #t)
		    2 1 #f)
  (spew-single-loop order-f4
		    (lambda (q) `(lie f 4 ,q))
		    (lambda (b e) #t)
		    2 1 #f)
  (spew-single-loop order-g2
		    (lambda (q) `(lie g 2 ,q))
		    (lambda (b e) (not (and (= b 2) (= e 1))))
		    2 1 #f)
  (spew-double-loop order-2an
		    (lambda (l q) `(lie 2a ,l ,(* q q)))
		    (lambda (l b e)
		      (not (and (<= l 3) (= b 2) (= e 1))))
		    2 2 1 #f #f)
  (spew-single-loop order-2b2
		    (lambda (q2) `(lie 2b 2 ,q2))
		    (lambda (b e) (and (= b 2)
				       (= (remainder e 2) 1)
				       (> e 1)))
		    2 1 #f)
  (spew-double-loop order-2dn
		    (lambda (l q) `(lie 2d ,l ,(* q q)))
		    (lambda (l b e) #t)
		    4 2 1 #f #f)
  (spew-single-loop order-3d4
		    (lambda (q) `(lie 3d 4 ,(power q 3)))
		    (lambda (b e) #t)
		    2 1 #f)
  (spew-single-loop order-2e6
		    (lambda (q) `(lie 2e 6 ,(* q q)))
		    (lambda (b e) #t)
		    2 1 #f)
  (spew-single-loop order-2f4
		    (lambda (q2) `(lie 2f 4 ,q2))
		    (lambda (b e) (and (= b 2)
				       (= (remainder e 2) 1)
				       (> e 1)))
		    2 1 #f)
  (spew-isolated '(tits 2f 4 2) (e-quotient (order-2f4 2) 2))
  (spew-single-loop order-2g2
		    (lambda (q2) `(lie 2g 2 ,q2))
		    (lambda (b e) (and (= b 3)
				       (= (remainder e 2) 1)
				       (> e 1)))
		    2 1 #f)
  (spew-isolated '(spor-m11) (* (power 2 4) (power 3 2) 5 11))
  (spew-isolated '(spor-m12) (* (power 2 6) (power 3 3) 5 11))
  (spew-isolated '(spor-m22) (* (power 2 7) (power 3 2) 5 7 11))
  (spew-isolated '(spor-m23) (* (power 2 7) (power 3 2) 5 7 11 23))
  (spew-isolated '(spor-m24) (* (power 2 10) (power 3 3) 5 7 11 23))
  (spew-isolated '(spor-j1) (* (power 2 3) 3 5 7 11 19))
  (spew-isolated '(spor-j2) (* (power 2 7) (power 3 3) (power 5 2) 7))
  (spew-isolated '(spor-j3) (* (power 2 7) (power 3 5) 5 17 19))
  (spew-isolated '(spor-j4) (* (power 2 21) (power 3 3) 5 7
			       (power 11 3) 23 29 31 37 43))
  (spew-isolated '(spor-hs) (* (power 2 9) (power 3 2) (power 5 3) 7 11))
  (spew-isolated '(spor-mc) (* (power 2 7) (power 3 6) (power 5 3) 7 11))
  (spew-isolated '(spor-sz) (* (power 2 13) (power 3 7) (power 5 2) 7 11 13))
  (spew-isolated '(spor-ly) (* (power 2 8) (power 3 7) (power 5 6)
			       7 11 31 37 67))
  (spew-isolated '(spor-he) (* (power 2 10) (power 3 3) (power 5 2)
			       (power 7 3) 17))
  (spew-isolated '(spor-ru) (* (power 2 14) (power 3 3) (power 5 3) 7 13 29))
  (spew-isolated '(spor-on) (* (power 2 9) (power 3 4) 5 (power 7 3) 11 19 31))
  (spew-isolated '(spor-co3) (* (power 2 10) (power 3 7) (power 5 3) 7 11 23))
  (spew-isolated '(spor-co2) (* (power 2 18) (power 3 6) (power 5 3) 7 11 23))
  (spew-isolated '(spor-co1) (* (power 2 21) (power 3 9) (power 5 4)
				(power 7 2) 11 13 23))
  (spew-isolated '(spor-f22) (* (power 2 17) (power 3 9) (power 5 2) 7 11 13))
  (spew-isolated '(spor-f23) (* (power 2 18) (power 3 13) (power 5 2)
				7 11 13 17 23))
  (spew-isolated '(spor-f24) (* (power 2 21) (power 3 16) (power 5 2)
				(power 7 3) 11 13 17 23 29))
  (spew-isolated '(spor-f3) (* (power 2 15) (power 3 10) (power 5 3)
				(power 7 2) 13 19 31))
  (spew-isolated '(spor-f5) (* (power 2 14) (power 3 6) (power 5 6)
				7 11 19))
  (spew-isolated '(spor-f2) (* (power 2 41) (power 3 13) (power 5 6)
				(power 7 2) 11 13 17 19 23 31 47))
  (spew-isolated '(spor-f1) (* (power 2 46) (power 3 20) (power 5 9)
				(power 7 6) (power 11 2) (power 13 3)
				17 19 23 29 31 41 47 59 71))
  )

;; Enumerate all finite simple groups whose order is less than bound.
(define (simplegroups bound)
  (let ((list '()))
    (define (add tag ord)
      (define (add-loop pre post)
	(if (and (not (null? post))
		 (>= ord (cdar post)))
	    (add-loop post (cdr post))
	    (if (null? pre)
		(set! list (cons `(,tag . ,ord) post))
		(set-cdr! pre (cons `(,tag . ,ord) post)))))
      (add-loop '() list))
    (spew-simplegroups bound add)
    list))

;; Produce an HTML-ized table.
(define (html-table file bound)
  (let ((list (simplegroups bound)))
    (display "<table>" file) (newline file)
    (map (lambda (pair)
	   (map display
		`("<tr><td>" ,(car pair) "</td><td>" ,(cdr pair) "</td></tr>")
		`(,file ,file ,file ,file ,file))
	   (newline file))
	 list)
    (display "</table>" file) (newline file)))
