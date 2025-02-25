;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname minimal-example) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
#lang clotho

(require xsmith
         racr
         racket/string)
 
(define-spec-component arith)
 
(add-to-grammar
 arith
 [Program #f (Expression)]
 [Expression #f ()
             #:prop may-be-generated #f]
 [LiteralInt Expression ([v = (random 100)])]
 [Addition Expression ([l : Expression]
                       [r : Expression])
           ;; The default weight is 10.
           #:prop choice-weight 20])
 
(define int (base-type 'int))
(add-property
 arith
 type-info
 [Program [int (λ (n t) (hash 'Expression int))]]
 [LiteralInt [int (λ (n t) (hash))]]
 [Addition [int (λ (n t) (hash 'l int 'r int))]])
 
(add-property
 arith
 render-node-info
 [Program
  (λ (n) (att-value 'xsmith_render-node (ast-child 'Expression n)))]
 [LiteralInt
  (λ (n) (number->string (ast-child 'v n)))]
 [Addition
  (λ (n) (format "(~a + ~a)"
                 (att-value 'xsmith_render-node (ast-child 'l n))
                 (att-value 'xsmith_render-node (ast-child 'r n))))])
 
;; This line defines `arith-command-line`.
(define-xsmith-interface-functions
  [arith]
  #:comment-wrap (λ (lines)
                   (string-join
                    (map (λ (x) (format "// ~a" x)) lines)
                    "\n")))
 
(module+ main (arith-command-line))