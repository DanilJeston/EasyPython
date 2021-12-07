# -*- coding: utf-8 -*-
from Scripts.Tokens import *
from Scripts.CustomErrors import *
from Scripts.Position import *


class Lexer:
    def __init__(self, fn, text: '用户输入文本'):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.read_next_char()

    def read_next_char(self):
        # 将pos增加1
        self.pos.read_next_char(self.current_char)
        if self.pos.idx < len(self.text):
            # 如果pos小于text的长度，读取用户输入文本
            self.current_char = self.text[self.pos.idx]
        else:
            # 否则设为None
            self.current_char = None

    def make_tokens_list(self):
        # 创造token列表
        tokens_list = []

        # 循环，当current_char 不等于 None 时
        while self.current_char is not None:
            if self.current_char in '\t ':
                self.read_next_char()

            elif self.current_char == '+':
                # 将 TT_PLUS 加入 Token 列表
                tokens_list.append(Token(TT_PLUS))
                self.read_next_char()

            elif self.current_char in DIGITS:
                tokens_list.append(self.make_number())

            elif self.current_char == '-':
                # 将 TT_MINUS 加入 Token 列表
                tokens_list.append(Token(TT_MINUS))
                self.read_next_char()

            elif self.current_char == '*':
                # 将 TT_MUL 加入 Token 列表
                tokens_list.append(Token(TT_MUL))
                self.read_next_char()

            elif self.current_char == '/':
                # 将 TT_DIV 加入 Token 列表
                tokens_list.append(Token(TT_DIV))
                self.read_next_char()

            elif self.current_char == '(':
                # 将 TT_LPAREN 加入 Token 列表
                tokens_list.append(Token(TT_LPAREN))
                self.read_next_char()

            elif self.current_char == ')':
                # 将 TT_RPAREN 加入 Token 列表
                tokens_list.append(Token(TT_RPAREN))
                self.read_next_char()

            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.read_next_char()
                return [], IllegalCharError(pos_start, self.pos, f"'{char}'")

        return tokens_list, None

    def make_number(self):
        # 将数字部分设为空字符串
        num_str = ''
        # 初始化计数小数点
        dot_count = 0

        # 当current_char不为None并且current_char在DIGITS中
        while self.current_char is not None and self.current_char in DIGITS + '.':
            # 如果检测到小数点
            if self.current_char == '.':
                if dot_count == 1:
                    break
                # 小数点+1
                dot_count += 1
                # num_str + "."
                num_str += '.'
            else:
                num_str += self.current_char
            self.read_next_char()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
