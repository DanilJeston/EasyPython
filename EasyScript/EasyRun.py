# -*- coding:utf-8 -*-
from EasyScript.EasyLexer import *

def run(text):
    lexers = Lexer(text)
    tokens, error = lexers.make_tokens()
    return tokens, error
