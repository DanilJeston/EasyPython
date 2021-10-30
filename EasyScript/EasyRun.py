# -*- coding:utf-8 -*-
from EasyScript.EasyLexer import *
from EasyScript.EasyParser import *

def run(fn, text):
    # 生成 Token
    lexers = Lexer(fn, text)
    tokens, error = lexers.make_tokens()
    if error: return None, error
    
    # 生成 AST
    parser = Parser(tokens)
    ast = parser.parse()
    
    return ast.node, ast.error
