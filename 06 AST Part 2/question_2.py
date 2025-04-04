"""
Given the grammar of MP as follows:

program: exp EOF;
exp: term ASSIGN exp | term;
term: factor COMPARE factor | factor;
factor: factor ANDOR operand | operand; 
operand: ID | INTLIT | BOOLIT | '(' exp ')';
INTLIT: [0-9]+ ;
BOOLIT: 'True' | 'False' ;
ANDOR: 'and' | 'or' ;
ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;
COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;
ID: [a-z]+ ;

and AST classes as follows:

class Expr(ABC):
class Binary(Expr):  #op:string;left:Expr;right:Expr
class Id(Expr): #value:string
class IntLiteral(Expr): #value:int
class BooleanLiteral(Expr): #value:boolean

Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return None

    def visitExp(self,ctx:MPParser.ExpContext):
        return None

    def visitTerm(self,ctx:MPParser.TermContext): 
        return None

    def visitFactor(self,ctx:MPParser.FactorContext):
        return None

    def visitOperand(self,ctx:MPParser.OperandContext):
        return None
"""

class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.ASSIGN():
            op = ctx.ASSIGN().getText()
            left = self.visit(ctx.term())
            right = self.visit(ctx.exp())
            return Binary(op, left, right)
        else:
            return self.visit(ctx.term())

    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            op = ctx.COMPARE().getText()
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            return Binary(op, left, right)
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.ANDOR():
            op = ctx.ANDOR().getText()
            left = self.visit(ctx.factor())
            right = self.visit(ctx.operand())
            return Binary(op, left, right)
        else:
            return self.visit(ctx.operand())

    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText())
        else:
            return self.visit(ctx.exp())