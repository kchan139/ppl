"""
Given the grammar of MP as follows:

program: mptype EOF;
arraytype:  primtype dimen | arraytype dimen  ;
mptype: primtype | arraytype;
primtype: INTTYPE | FLOATTYPE; 
dimen: '[' num '..' num ']';
num: '-'? INTLIT;
INTLIT: [0-9]+ ;
INTTYPE: 'integer';
FLOATTYPE: 'real';

and AST classes as follows:

class Type():abstract
class CompoundType(Type):abstract
class UnionType(CompoundType):#firstType:Type,secondType:primType
class ArrayType(CompoundType):#indexType:Type,eleType:primType
class PrimType(Type):abstract
class IntType(PrimType): pass
class FloatType(PrimType): pass
class RangeType(PrimType): #lowbound:int; highbound:int

Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return None

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return None

    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        return None

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        return None

    def visitDimen(self,ctx:MPParser.DimenContext):
        return None

    def visitNum(self,ctx:MPParser.DimenContext):
        return None
"""