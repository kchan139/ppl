grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}


//====== Q1 ======//
// program
// 	: (vardecl | funcdecl)+ EOF
// 	;	// write for program rule here using vardecl and funcdecl

// vardecl
// 	: 'vardecl' 
// 	;

// funcdecl
// 	: 'funcdecl' 
// 	;

//====== Q2 ======//
// program
// 	: (vardecl | funcdecl)+ EOF
// 	; // write your rule here

// //And some other rules for variable declaration, function declaration and other rules
// typedecl
// 	: INT | FLOAT
// 	;
// idlist
// 	: ID (COMMA ID)*
// 	;
// paramlist
// 	: typedecl idlist
// 	;
// paramdecl
// 	: LPAREN paramlist* (SEMICOLON paramlist)* RPAREN
// 	;
// vardecl
// 	: typedecl idlist SEMICOLON
// 	;
// funcdecl
// 	: typedecl ID paramdecl body
// 	;
// body
// 	: 'body'
// 	;




//====== Q3 ======//
// program
// 	: (vardecl | funcdecl)+ EOF
// 	; // write your rule here

// //And some other rules for variable declaration, function declaration and other rules
// typedecl
// 	: INT | FLOAT
// 	;
// idlist
// 	: ID (COMMA ID)*
// 	;
// paramlist
// 	: typedecl idlist
// 	;
// paramdecl
// 	: LPAREN paramlist* (SEMICOLON paramlist)* RPAREN
// 	;
// vardecl
// 	: typedecl idlist SEMICOLON
// 	;
// funcdecl
// 	: typedecl ID paramdecl body
// 	;
// body
// 	: LBRACK (vardecl | statement)* RBRACK
// 	;
// statement
// 	: ID ASSIGN expr SEMICOLON							# assign
// 	| ID LPAREN expr* (COMMA expr)* RPAREN SEMICOLON	# function_method_call
// 	| RETURN expr	SEMICOLON							# return
// 	;
// expr
// 	: 'expr'
// 	;


//====== Q4 ======//
program
	: (vardecl | funcdecl)+ EOF
	; // write your rule here

//And some other rules for variable declaration, function declaration and other rules
typedecl
	: INT | FLOAT
	;
idlist
	: ID (COMMA ID)*
	;
paramlist
	: typedecl idlist
	;
paramdecl
	: LPAREN paramlist* (SEMICOLON paramlist)* RPAREN
	;
vardecl
	: typedecl idlist SEMICOLON
	;
funcdecl
	: typedecl ID paramdecl body
	;
body
	: LBRACK (vardecl | statement)* RBRACK
	;
statement
	: ID ASSIGN expr SEMICOLON							# assign
	| ID LPAREN expr* (COMMA expr)* RPAREN SEMICOLON	# function_method_call
	| RETURN expr	SEMICOLON							# return
	;
expr
	: 'expr'
	;




INT
	: 'int'
	;
FLOAT
	: 'float'
	;
COMMA
	: ','
	;
SEMICOLON
	: ';'
	;
LPAREN
	: '('
	;
RPAREN
	: ')'
	;
LBRACK
	: '{'
	;
RBRACK
	: '}'
	;
ASSIGN
	: '='
	;
RETURN
	: 'return'
	;
ID
	: [a-zA-Z]+
	; // includes a sequence of alphabetic characters.
WS
	: [ \t\r\n] -> skip
	;
ERROR_CHAR
	: . {raise ErrorToken(self.text)}
	;