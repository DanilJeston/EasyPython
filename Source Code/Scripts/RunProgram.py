from Scripts.Lexer import *

releaseMode = True


def run(fn, text):
    # 实例化Lexer
    lexer = Lexer(fn, text)
    # 获取Token_list
    tokens_list, error = lexer.make_tokens_list()
    if not releaseMode:
        print(tokens_list)

    return tokens_list, error