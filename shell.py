# -*- coding:utf-8 -*-
from EasyScript.EasyTokens import *
from EasyScript.EasyLexer import *
from EasyScript.EasyPyErrors import *
from EasyScript.EasyRun import *
import sys

def shell():
    while True:
        text = input("EasyPy > ")
        if text == 'exit':
            print('GoodBye!')
            sys.exit()
        else:
            result, error = run(text)
        
        if error:
            print(error.as_string())
        else:
            print(result)

shell()