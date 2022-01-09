# -*- coding:utf-8 -*-
from EasyScript.EasySymbolTable import *
from EasyScript.EasyTokens import *

global_symbol_table = SymbolTable()
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