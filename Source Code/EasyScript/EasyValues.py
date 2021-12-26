# -*- coding:utf-8 -*-
from EasyScript.EasyPyErrors import *
import EasyScript.EasyInterpreter as EasyInterpreter
from EasyScript.EasyRuntimeResult import *
from EasyScript.EasyContext import *
from EasyScript.EasySymbolTable import *
import os


class Value:
    def __init__(self, type_):
        self.type = type_
        self.set_pos()
        self.set_context()

    def set_context(self, context=None):
        self.context = context
        return self

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def added_to(self, other):
        return None, self.illegal_operation(other)

    def subbed_by(self, other):
        return None, self.illegal_operation(other)

    def multed_by(self, other):
        return None, self.illegal_operation(other)

    def dived_by(self, other):
        return None, self.illegal_operation(other)

    def powed_by(self, other):
        return None, self.illegal_operation(other)

    def copy(self):
        raise Exception('No copy method defined')

    def get_comparison_eq(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other):
        return None, self.illegal_operation(other)

    def anded_by(self, other):
        return None, self.illegal_operation(other)

    def is_true(self):
        return self.value != 0

    def ored_by(self, other):
        return None, self.illegal_operation(other)

    def notted(self):
        return None, self.illegal_operation()

    def execute(self, args):
        return None, self.illegal_operation()

    def illegal_operation(self, other=None):
        if not other:
            other = self
        return RTError(self.pos_start, other.pos_end, 'Illegal operation',
                       self.context)

    def __repr__(self):
        return str(self.value)


class Number(Value):
    def __init__(self, value):
        super().__init__("number")
        self.value = value

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(other.pos_start, other.pos_end,
                                     "Division by zero", self.context)
            return Number(self.value / other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value**other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            # if self.value > other.value:
            #     print(self.value)
            #     print(other.value)
            #     print(self.value > other.value)
            #     return Number(1)
            # else:
            #     return Number(0)
            return Number(int(self.value > other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value
                              and other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def is_true(self):
        return self.value != 0

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value
                              or other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(
            self.context), None

    def __repr__(self):
        return str(self.value)


Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)


class String(Value):
    def __init__(self, value):
        super().__init__("string")
        self.value = value

    def added_to(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
        if isinstance(other, String):
            return Number(int(self.value == other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        if isinstance(other, String):
            return Number(int(self.value != other.value)).set_context(
                self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def is_true(self):
        return len(self.value) > 0

    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return f'"{self.value}"'


class List(Value):
    def __init__(self, elements):
        super().__init__("list")
        self.elements = elements

    def added_to(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def subbed_by(self, other):
        if isinstance(other, Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    "Element at this index could not be remove from list because index is out of bounds",
                    self.context)
        else:
            return None, Value.illegal_operation(self, other)

    def multed_by(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    "Element at this index could not be retrieved from list because index is out of bounds",
                    self.context)
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = List(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self):
        return f'[{", ".join([str(x) for x in self.elements])}]'


class BaseFunction(Value):
    def __init__(self, name):
        super().__init__('function')
        self.name = name or "<anonymous>"

    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, arg_names, args):
        res = RTResult()

        if len(args) > len(arg_names):
            return res.failure(
                RTError(
                    self.pos_start, self.pos_end,
                    f"{len(args) - len(arg_names)} too many args passed into '{self.name}'",
                    self.context))

        if len(args) < len(arg_names):
            return res.failure(
                RTError(
                    self.pos_start, self.pos_end,
                    f"{len(arg_names) - len(args)} too few args passed into '{self.name}'",
                    self.context))

        return res.success(None)

    def populate_args(self, arg_names, args, exec_ctx):

        for i in range(len(args)):
            arg_name = arg_names[i]
            arg_value = args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def check_and_populate_args(self, args_name, args, exec_ctx):
        res = RTResult()
        res.register(self.check_args(args_name, args))
        if res.error:
            return res
        self.populate_args(args_name, args, exec_ctx)
        return res.success(None)


class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names

    def execute(self, args):
        res = RTResult()
        interpreter = EasyInterpreter.Interpreter()
        exec_ctx = self.generate_new_context()

        res.register(
            self.check_and_populate_args(self.arg_names, args, exec_ctx))
        if res.error:
            return res

        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        if res.error:
            return res
        return res.success(value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"


class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)

    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()

        method_name = f'execute_{self.name}'
        method = getattr(self, method_name, self.no_visit_method)

        res.register(
            self.check_and_populate_args(method.arg_names, args, exec_ctx))
        if res.error:
            return res

        return_value = res.register(method(exec_ctx))
        if res.error:
            return res

        return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f"No execute_{self.name} method defined")

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<built-in function {self.name}>"

    # 内建函数开始
    """
    函数格式:
    exec_ctx: 用于获取参数，使用: exec_ctx.symbol_table.get("<参数名>")
    def execute_<函数名>(self, exec_ctx):
        <代码>
        return RTResult().success(<String/Number/List>(<None或者返回值>))
    execute_<函数名>.arg_names = ["<参数名1>", "<参数名2>..."]
    结束
    完成后请记得在文件底部添加 BuiltInFunction.<函数名> = BuiltInFunction("<函数名>")
    以及在EasyRun.py中使用 global_symbol_table.set('<函数名>', BuiltInFunction.<函数名>)
    最后还要在EasyTokens.py中的 BuiltInFunctionList 添加'函数名'
    """

    def execute_println(self, exec_ctx):
        print(str(exec_ctx.symbol_table.get("value").value))
        return RTResult().success(None)

    # # 需要参数: 'value'
    execute_println.arg_names = ["value"]

    def execute_printf(self, exec_ctx):
        print(str(exec_ctx.symbol_table.get("value").value), end="")
        return RTResult().success(None)

    execute_printf.arg_names = ['value']

    def execute_input(self, exec_ctx):
        text = input()
        return RTResult().success(String(text))

    execute_input.arg_names = []

    def execute_clear(self, exec_ctx):
        os.system('cls' if os.name == 'nt' else 'clear')
        return RTResult().success(None)

    execute_clear.arg_names = []

    def execute_is_number(self, exec_ctx):
        is_number = isinstance(exec_ctx.symbol_table.get("value"), Number)
        return RTResult().success(Number.true if is_number else Number.false)

    execute_is_number.arg_names = ['value']

    def execute_is_string(self, exec_ctx):
        is_string = isinstance(exec_ctx.symbol_table.get("value"), String)
        return RTResult().success(Number.true if is_string else Number.false)

    execute_is_string.arg_names = ['value']

    def execute_is_list(self, exec_ctx):
        is_list = isinstance(exec_ctx.symbol_table.get("value"), List)
        return RTResult().success(Number.true if is_list else Number.false)

    execute_is_list.arg_names = ['value']

    def execute_is_function(self, exec_ctx):
        is_function = isinstance(exec_ctx.symbol_table.get("value"),
                                 BaseFunction)
        return RTResult().success(Number.true if is_function else Number.false)

    execute_is_function.arg_names = ['value']

    def execute_append(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")
        # print(exec_ctx.symbol_table.symbols)

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end,
                        "First argumrnt must be list", exec_ctx))

        list_.elements.append(value)
        return RTResult().success(list_)

    execute_append.arg_names = ['list', 'value']

    def execute_pop(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")

        if not isinstance(list_, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end,
                        "First argumrnt must be list", exec_ctx))

        if not isinstance(index, Number):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end,
                        "Second argumrnt must be number", exec_ctx))

        try:
            elements = list_.elements.pop(index.value)
        except:
            return RTResult().failure(
                RTError(
                    self.pos_start, self.pos_end,
                    "Element at this index could not be removed from list because index is out of bounds",
                    exec_ctx))
        return RTResult().success(elements)

    execute_pop.arg_names = ['list', 'index']

    def execute_extend(self, exec_ctx):
        listA = exec_ctx.symbol_table.get("listA")
        listB = exec_ctx.symbol_table.get("listB")

        if not isinstance(listA, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end,
                        "First argumrnt must be list", exec_ctx))

        if not isinstance(listB, List):
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end,
                        "Second argumrnt must be list", exec_ctx))

        listA.elements.extend(listB.elements)
        return RTResult().success(listA)

    execute_extend.arg_names = ['listA', 'listB']

    def execute_str(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        return RTResult().success(String(value))

    execute_str.arg_names = ['value']

    def execute_int(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        try:
            return_value = int(value.value)
        except ValueError:
            return RTResult().failure(
                RTError(self.pos_start, self.pos_end,
                        f"invalid literal for int() with base 10: {value}",
                        self.context))
        return RTResult().success(Number(return_value))

    execute_int.arg_names = ['value']

    def execute_type(self, exec_ctx):
        value = exec_ctx.symbol_table.get("value")
        return RTResult().success(String(f"<class {value.type}>"))

    execute_type.arg_names = ['value']


BuiltInFunction.type = BuiltInFunction("type")
BuiltInFunction.str = BuiltInFunction("str")
BuiltInFunction.int = BuiltInFunction("int")
BuiltInFunction.printf = BuiltInFunction("printf")
BuiltInFunction.println = BuiltInFunction("println")
BuiltInFunction.input = BuiltInFunction("input")
BuiltInFunction.clear = BuiltInFunction("clear")
BuiltInFunction.is_number = BuiltInFunction("is_number")
BuiltInFunction.is_string = BuiltInFunction("is_string")
BuiltInFunction.is_list = BuiltInFunction("is_list")
BuiltInFunction.is_function = BuiltInFunction("is_function")
BuiltInFunction.append = BuiltInFunction("append")
BuiltInFunction.pop = BuiltInFunction("pop")
BuiltInFunction.extend = BuiltInFunction("extend")
