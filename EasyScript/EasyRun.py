# -*- coding:utf-8 -*-
from EasyScript.EasyLexer import *
from EasyScript.EasyParser import *
from EasyScript.EasyInterpreter import *
from EasyScript.EasyContext import *
from EasyScript.EasySymbolTable import *

global_symbol_table = SymbolTable()
global_symbol_table.set('NULL', Number(0))
global_symbol_table.set('TRUE', Number(1))
global_symbol_table.set('FALSE', Number(0))


def run(fn, text):
    # 生成 Token
    lexers = Lexer(fn, text)
    tokens, error = lexers.make_tokens()
    if error: 
        return None, error
    
    # 生成 AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error
    
    
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)
    
    
    return result.value, result.error
