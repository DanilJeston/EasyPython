# -*- coding:utf-8 -*-
from Scripts import *
import sys


def shell():
    while True:
        command = input('EasyPy >>> ')
        result, error = run('<stdin>', command)

        if command == 'exit':
            print("Good bye, Thanks for using.")
            sys.exit(0)

        if error:
            print(error.as_string())
        elif result:
            print(result)

if __name__ == '__main__':
    shell()
