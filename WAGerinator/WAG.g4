grammar WAG;

//Root element
wag : comment? metadata? rule*;
// PARSER GRAMMAR
// Metadata Section
metadata           : meta* META_END;
meta               : include | config;
include            : IDENTIFIER? INCLUDEDECL IDENTIFIER include? STATEMENT_END;
config             : IDENTIFIER DECLARATION IDENTIFIER STATEMENT_END;

comment            : '/*' ~('\r' | '*/')* '*/';

// Production Rules
rule               : IDENTIFIER nTArgs? PROPESITION_SIGN rhs STATEMENT_END;
rhs                : weight? chunk* EBNF_OPTION rhs | weight? chunk* ;
weight             : BRACKET_L attrIdentifier? expression BRACKET_R;
chunk              : chunkP EBNFTYPE?;
chunkP             : symbol
	               |  LPAREN chunk* RPAREN
	               ;
symbol             :  nonTerminal
                   |  terminal
                   |  assignment
                   ;

terminal : STRING | FLOAT | BOOL | INT;
nonTerminal        : IDENTIFIER EBNFTYPE?;
nTArgs             : LEFT_ANGLE_BRACKET attrIdentifierList RIGHT_ANGLE_BRACKET;
attrIdentifier     : ATTRSPEC? IDENTIFIER;
attrIdentifierList : attrIdentifier DELIMITER attrIdentifierList
                   |  attrIdentifier
                   |  STRING
                   ;

assignment         : nTAssigment | attributeAssignment;
nTAssigment        : nonTerminal nTArgs EBNFTYPE?;
attributeAssignment: ATTR_ASSIGN_L (attrIdentifier EQ expression STATEMENT_END?)* ATTR_ASSIGN_R;

// Attribute Evaluation
expression         : SUBPROC
                   |  if
                   |  disjunct
                   ;

if                 : IF ifStatement THEN disjunct (ELSE expression)?;
ifStatement        : disjunct | boolInverse | BOOL;

disjunct           : conjunct (AND disjunct)?;
conjunct           : inverse (OR conjunct)?;
inverse            : INVERSE_SIGN? comparison;
comparison         : sum (compop sum)?;
sum                : term sumP?;
sumP               : SUMOP term sumP?;
term               : factor termP?;
termP              : TERMOP factor termP?;
factor             : atom (FACTORIAL factor)?;
atom               : attrIdentifier
                   | dictonary
                   | BOOL
                   | boolInverse
                   |  FLOAT
                   |  INT
                   |  STRING
                   |  LPAREN expression RPAREN
                   ;

dictonary   : BRACKET_L expression BRACKET_R;
compop      : LEFT_ANGLE_BRACKET | LEQ | RIGHT_ANGLE_BRACKET | GEQ | EQ2 | NEQ | IN;
boolInverse : INVERSE_SIGN BOOL;

// Lexer
IF                 : 'if';
ELSE               : 'else';
THEN               : 'then';
AND                : '&&';
OR                 : '||';
FACTORIAL          : '**';
LEQ                : '<=';
GEQ                : '>=';
EQ2                : '==';
NEQ                : '!=';
IN                 : 'in';

INCLUDEDECL        : '::';
PROPESITION_SIGN   : '->';
BOOL               : 'true' | 'false';
IDENTIFIER         : [a-zA-Z][a-zA-Z0-9_]*;
ATTRSPEC           : '$' | '*' | '&';
TERMOP             : '*' | '//' | '/' | '%';
SUMOP              : '+' | '-';
EBNFTYPE           : '@' | '~' | '?';
INT                : NUM+;
NUM                : [0-9];
FLOAT              : [0-9]*'.'[0-9]*;
STRING             : '"' ~('\r' | '\n' | '"')* '"'
                   | '\'' ~('\r' | '\n' | '"')* '\'';

EBNF_OPTION        : '#';
SUBPROC            : '$( /[^)]*/ )';
DECLARATION        : ':';
STATEMENT_END      : ';';
EQ                 : '=';
META_END           : '****';
INVERSE_SIGN       : '!';
BRACKET_L          : '[';
BRACKET_R          : ']';
ATTR_ASSIGN_L      : '{';
ATTR_ASSIGN_R      : '}';
LPAREN             : '(';
RPAREN             : ')';
LEFT_ANGLE_BRACKET : '<';
RIGHT_ANGLE_BRACKET: '>';
DELIMITER          : ',';



