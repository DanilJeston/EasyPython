'''
Author: __init__(PartyParrot)
Github: https://github.com/PartyParrot359
Date: 2021-11-19 13:09:34
LastEditors: __init__(PartyParrot)
LastEditTime: 2021-11-19 13:12:33

作用为上下文
在 TraceBack中会显示
'''


class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None
