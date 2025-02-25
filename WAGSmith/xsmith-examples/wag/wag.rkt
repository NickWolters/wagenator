#lang clotho

(require
 xsmith
 xsmith/app
 racr
 xsmith/racr-convenience
 xsmith/canned-components
 (except-in pprint empty)
 racket/format
 racket/string
 racket/match
 
 syntax/parse/define
 "../private/util.rkt"
 "../private/xsmith-examples-version.rkt"
 (for-syntax
  racket/base
  syntax/parse
  ))

(define-basic-spec-component wag-comp)

(define number-type (base-type 'number #:leaf? #f))
(define real-type (base-type 'real number-type #:leaf? #f))
(define int-type (base-type 'int real-type))
(define float-type (base-type 'float real-type))
(define char-type (base-type 'char))


(add-basic-expressions wag-comp
                       #:VariableReference #t
                       #:ProcedureApplication #t
                       #:int-type int-type
                       #:number-type number-type
                       #:index-and-length-type int-type
                       #:Numbers #t
                       #:Booleans #t
                       #:Strings #t
                       #:MutableArray #t
                       #:MutableStructuralRecord #t
                      )
(add-basic-statements wag-comp
                      #:ProgramWithBlock #t
                      #:Block #t
                      ; #:IfElseStatement #t
                      #:ExpressionStatement #t
                      #:AssignmentStatement #t
                      #:int-type int-type
                      #:MutableArraySafeAssignmentStatement #t
                      #:MutableStructuralRecordAssignmentStatement #t
                    )

(define nest-step 4)

(define (render-child fieldname n)
  (att-value 'xsmith_render-node (ast-child fieldname n)))
(define (binary-function-renderer name)
  (λ (n) (h-append (text name) (text "(")
                   (render-child 'l n) (text ", ") (render-child 'r n)
                   (text ")"))))
(define (binary-op-renderer op-rendered)
  (λ (n) (h-append lparen (render-child 'l n)
                   space op-rendered space
                   (render-child 'r n) rparen)))                      


; (add-to-grammar
;  wag-comp

;  [WeightStatement Expression (Expression)
;    #:prop type-info
;       [string-type (λ (n t) (hash 'Expression (char-type)))]
;     #:prop render-node-info
;       (λ (n)(h-append (text "[") space (att-value 'xsmith_render-node (ast-child 'test n)) space)
;         (att-value 'xsmith_render-node (ast-child 'then n))
;         (text "]")
;   )]
; )    



(add-property
 wag-comp
 render-hole-info
 [#f (λ (h) (text "«HOLE»"))])

(define (comma-list doc-list)
  (apply h-append
         (apply-infix (h-append comma space)
                      doc-list)))


(add-property
 wag-comp
 render-node-info

 [ProgramWithBlock
  (λ (n)
    (define definitions (ast-children (ast-child 'definitions n)))
    (v-append
     (text "****")
     (text "Start of the generated WAG Code.")
     (text "****")
     (vb-concat
      (list*
       (text "")
       (text "")
       (map (λ (cn) (att-value 'xsmith_render-node cn))
            (append definitions
                    (list (ast-child 'Block n))))))
     (text "")
    ))]

 [Block
  (λ (n)
    (h-append
     lbrace
     (nest nest-step
           (h-append
            line
            (v-concat
             (append
              (map (λ (cn) (att-value 'xsmith_render-node cn))
                   (ast-children (ast-child 'definitions n)))
              (map (λ (cn) (att-value 'xsmith_render-node cn))
                   (ast-children (ast-child 'statements n)))))))
     line
     rbrace))]     

 [Definition (λ (n)
               (h-append (text (ast-child 'name n))
                         space
                         equals
                         space
                         (att-value 'xsmith_render-node (ast-child 'Expression n))
                         semi))]

   [ExpressionStatement (λ (n) (h-append (att-value 'xsmith_render-node (ast-child 'Expression n))
                                         semi))]                       

  [AssignmentStatement
   (λ (n)
     (h-append (text (format "~a" (ast-child 'Expression n)))
               space
               (text "->")
               space
               (att-value 'xsmith_render-node (ast-child 'Expression n))
               semi))]

;  [IfElseStatement
;   (λ (n)
;     (h-append
;      (h-append (text "if") space (att-value 'xsmith_render-node (ast-child 'test n)) space)
;      (att-value 'xsmith_render-node (ast-child 'then n))
;      (text "else")
;      (att-value 'xsmith_render-node (ast-child 'else n))))]

 [VariableReference (λ (n) (text (format "~a" (ast-child 'name n))))]

 [BoolLiteral (λ (n) (text (if (ast-child 'v n) "true" "false")))]
 [Not (λ (n) (h-append (text "!") lparen
                       ($xsmith_render-node (ast-child 'Expression n))
                       rparen))]
 [And (binary-op-renderer (text "&&"))]
 [Or (binary-op-renderer (text "||"))]

 [IntLiteral (λ (n) (text (format "~a" (ast-child 'v n))))]
 [Plus (binary-op-renderer '+)]
 [Minus (binary-op-renderer '-)]
 [Times (binary-op-renderer '*)]

 ;;[Divide (binary-op-renderer '/)]

 [LessThan (binary-op-renderer (text "<"))]
 [GreaterThan (binary-op-renderer (text ">"))]

 [StringLiteral (λ (n) (text (format "~v" (ast-child 'v n))))]
 [StringLength (λ (n) (h-append lparen
                                (att-value 'xsmith_render-node (ast-child 'Expression n))
                                rparen
                                (text ".length")))]

  [MutableArrayLiteral
  (λ (n) (h-append lbracket
                   (comma-list (map (λ (cn) (att-value 'xsmith_render-node cn))
                                    (ast-children (ast-child 'expressions n))))
                   rbracket))]
 [MutableArraySafeReference
  (λ (n)
    (h-append (text "array_safe_reference(")
              (att-value 'xsmith_render-node (ast-child 'array n))
              (text ", ")
              (att-value 'xsmith_render-node (ast-child 'index n))
              (text ", ")
              (att-value 'xsmith_render-node (ast-child 'fallback n))
              (text ")")))]
 [MutableArraySafeAssignmentStatement
  (λ (n)
    (h-append (text "array_safe_assignment(")
              (att-value 'xsmith_render-node (ast-child 'array n))
              (text ", ")
              (att-value 'xsmith_render-node (ast-child 'index n))
              (text ", ")
              (att-value 'xsmith_render-node (ast-child 'newvalue n))
              (text ");")))]

 [MutableStructuralRecordLiteral
  (λ (n)
    ;; We need to wrap it in parentheses in statement contexts.
    (h-append lparen lbrace
              (comma-list (map (λ (fieldname expression-node)
                                 (h-append (text (format "~a" fieldname))
                                           colon
                                           space
                                           (att-value 'xsmith_render-node expression-node)))
                               (ast-child 'fieldnames n)
                               (ast-children (ast-child 'expressions n))))
              rbrace rparen))]
 [MutableStructuralRecordReference
  (λ (n) (h-append (att-value 'xsmith_render-node (ast-child 'record n))
                   (text ".")
                   (text (format "~a" (ast-child 'fieldname n)))))]
 [MutableStructuralRecordAssignmentStatement
  (λ (n) (h-append (att-value 'xsmith_render-node (ast-child 'record n))
                   (text ".")
                   (text (format "~a" (ast-child 'fieldname n)))
                   space equals space
                   (att-value 'xsmith_render-node (ast-child 'newvalue n))
                   semi))]                               
)

(add-loop-over-container
 wag-comp
 #:name ForLoopOverArray
 #:collection-type-constructor (λ (elem-type) (mutable (array-type elem-type)))
 #:loop-type-constructor (λ (elem-type) no-return-type)
 #:body-type-constructor (λ (loop-type elem-type) loop-type)
 #:mutable-container-access (read 'MutableArray)
 #:loop-ast-type Statement
 #:body-ast-type Block
 #:bind-whole-collection? #t
 )


(define (type-thunks-for-concretization)
  (list
   (λ()int-type)
   (λ()bool-type)
   (λ()string-type)
   (λ()char-type)
   ))

(define (wag-format-render doc)
  (pretty-format doc 120))

(define-xsmith-interface-functions
  [wag-comp]
  #:fuzzer-name wag
  #:fuzzer-version xsmith-examples-version-string/no-name
  #:type-thunks type-thunks-for-concretization
  #:program-node ProgramWithBlock
  #:format-render wag-format-render
  #:default-max-depth 8
  #:comment-wrap (λ (lines) (string-join (map (λ (l) (format "**** ~a" l)) lines)
                                         "\n")))
(module+ main (wag-command-line))
