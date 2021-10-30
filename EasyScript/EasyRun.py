# -*- coding:utf-8 -*-
from EasyScript.EasyLexer import *

def run(fn, text):
    lexers = Lexer(fn, text)
    tokens, error = lexers.make_tokens()
    return tokens, error
