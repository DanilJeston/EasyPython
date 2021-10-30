# -*- coding:utf-8 -*-
from EasyScript.EasyLexer import *
from EasyScript.EasyParser import *
from EasyScript.EasyInterpreter import *
from EasyScript.EasyContext import *

def run(fn, text):
    # 生成 Token
    lexers = Lexer(fn, text)
    tokens, error = lexers.make_tokens()
    if error: return None, error
    
    # 生成 AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:return None,ast.error
    
    
    interpreter =Interpreter()
    context = Context('<program>')
    result = interpreter.visit(ast.node, context)
    
    
    return result.value, result.error
