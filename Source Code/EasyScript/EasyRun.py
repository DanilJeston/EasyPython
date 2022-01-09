# -*- coding:utf-8 -*-
'''
作者: __init__(PartyParrot)
Github 地址: https://github.com/PartyParrot359
Gitee 地址: https://gitee.com/JUST_SANS
邮件: 2100970361@qq.com
Date: 2021-11-19 13:29:08
最后一次编辑人: __init__(PartyParrot)
LastEditTime: 2021-11-19 16:50:58
'''
# 导入库
from EasyScript.EasyLexer import *
from EasyScript.EasyParser import *
from EasyScript.EasyInterpreter import *
from EasyScript.EasyContext import *
from EasyScript.EasySymbolTable import *
from EasyScript.EasyTokens import *
import yaml


def SetGlobalSymbol(name, value, IsBuiltInFunction=False):
    global global_symbol_table
    if IsBuiltInFunction:
        global BuiltInFunctionList
        global_symbol_table.set(name, value)
        BuiltInFunctionList.append(name)
    else:
        global BuiltInIdentifierList
        global_symbol_table.set(name, value)
        BuiltInIdentifierList.append(name)


# 生成变量表
global_symbol_table = SymbolTable()
SetGlobalSymbol('Null', Number.null)
SetGlobalSymbol('input_tip', BuiltInFunction.input_tip)
SetGlobalSymbol('True', Number.true)
SetGlobalSymbol('False', Number.false)
SetGlobalSymbol('println', BuiltInFunction.println, True)
SetGlobalSymbol('printf', BuiltInFunction.printf, True)
SetGlobalSymbol('str', BuiltInFunction.str, True)
SetGlobalSymbol('type', BuiltInFunction.type, True)
SetGlobalSymbol('int', BuiltInFunction.int, True)
SetGlobalSymbol('input', BuiltInFunction.input, True)
SetGlobalSymbol('clear', BuiltInFunction.clear, True)
SetGlobalSymbol('is_num', BuiltInFunction.is_number, True)
SetGlobalSymbol('is_number', BuiltInFunction.is_number, True)
SetGlobalSymbol('is_str', BuiltInFunction.is_string, True)
SetGlobalSymbol('is_string', BuiltInFunction.is_string, True)
SetGlobalSymbol('is_list', BuiltInFunction.is_list, True)
SetGlobalSymbol('is_func', BuiltInFunction.is_function, True)
SetGlobalSymbol('is_function', BuiltInFunction.is_function, True)
SetGlobalSymbol('append', BuiltInFunction.append, True)
SetGlobalSymbol('pop', BuiltInFunction.pop, True)
SetGlobalSymbol('extend', BuiltInFunction.extend, True)
SetGlobalSymbol('float', BuiltInFunction.float, True)
releaseMode = yaml.safe_load(
    open("EasyScript/config.yml").read())['options']['release-mode']


# 创建函数 run
def run(fn, text):
    # 实例化 Lexer
    lexers = Lexer(fn, text)
    # 获取 tokens 和 error
    tokens, error = lexers.make_tokens()
    if error:
        return None, error
    if not releaseMode:
        print(tokens)

    # 实例化 parser
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error

    # 实例化 Interpreter
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    # print(ast.node)
    # print(type(ast.node).__name__)
    result = interpreter.visit(ast.node, context)

    # 返回值和错误
    return result.value, result.error
