'''
作者: __init__(PartyParrot)
Github 地址: https://github.com/PartyParrot359
Gitee 地址: https://gitee.com/JUST_SANS
邮件: 2100970361@qq.com
Date: 2021-11-19 14:38:39
最后一次编辑人: __init__(PartyParrot)
LastEditTime: 2021-11-19 14:38:39
'''
# -*- coding:utf-8 -*-
import string

# CONSTANTS 常量

# 数字
DIGITS = '0123456789'

# 字母
LETTERS = string.ascii_letters

# 数字 + 字母
LETTERS_DIGITS = LETTERS + DIGITS

# TOKEN

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_STRING = 'STRING'
TT_IDENTIFIER = 'IDENTIFIER'
TT_KEYWORD = 'KEYWORD'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_POW = 'POW'
TT_EQ = 'EQ'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_LSQUARE = 'LSQUARE'
TT_RSQUARE = 'RSQUARE'
TT_EE = 'EE'
TT_NE = 'NE'
TT_LT = 'LT'
TT_GT = 'GT'
TT_LTE = 'LTE'
TT_GTE = 'GTE'
TT_COMMA = 'COMMA'
TT_ARROW = 'ARROW'
TT_NEWLINE = 'NEWLINE'
TT_EOF = 'EOF'

KEYWORDS = [
    'define', 'and', 'or', 'not', 'if', 'then', 'elif', 'else', 'for', 'to',
    'step', 'while', 'function', 'end', 'import'
]

BuiltInFunctionList = []
BuiltInIdentifierList = []
PackageName = ['math']


class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
