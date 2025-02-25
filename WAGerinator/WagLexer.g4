lexer grammar WagLexer;

// Lexer

INCLUDEDECL        : '::';

PROPESITION_SIGN   : '->';

IDENTIFIER         : [a-zA-Z][a-zA-Z0-9_]*;

ATTRSPEC           : '$' | '*' | '&';

TERMOP             : '*' | '//' | '/' | '%';

SUMOP              : '+' | '-';

EBNFTYPE           : '@' | '~' | '?';

BOOL               : 'true' | 'false';

NUM                : [0-9];

FLOAT              : [0-9]*'.'[0-9]*;

STRING             : '"' ~('\r' | '\n' | '"')* '"'

                   | '\'' ~('\r' | '\n' | '"')* '\'';

EBNF_OPTION        : '|';

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

IN                 : 'in' | 'IN';