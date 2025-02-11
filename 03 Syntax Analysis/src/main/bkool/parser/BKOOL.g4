grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  :  EOF ;

ID: [a-z]+ ;
INTLIT:[0-9]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
