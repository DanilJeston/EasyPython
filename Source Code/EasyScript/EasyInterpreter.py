# -*- coding:utf-8 -*-
"""
Author: __init__(PartyParrot)
Github: https://github.com/PartyParrot359
Date: 2021-11-19 13:11:11
LastEditors: __init__(PartyParrot)
LastEditTime: 2021-11-19 13:11:11
定义 Interpreter 类
作用:
解释程序，处理方法
"""

# 导入库
from EasyScript.EasyValues import *
from EasyScript.EasyTokens import *
from EasyScript.EasyRuntimeResult import *


class Interpreter:
    def visit(self, node, context):
        """
        visit: 调用方法
        node: 提供节点，获取 __name__ 信息
        context: 上下文
        """
        method_name = f'visit_{type(node).__name__}'  # 定义 method_name
        # 从 self 类中寻找 method_name ，如果存在执行，反之调用 no_visit_method
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    def visit_VarAccessNode(self, node, context):
        """
        node: 节点，提供变量名
        """
        # 实例化运行时
        res = RTResult()
        var_name = node.var_name_tok.value
        # 从symbol_table获取变量值
        value = context.symbol_table.get(var_name)

        # 如果 value 是空的
        if not value:
            """
            返回运行时错误
            node.pos_start: 错误开始处
            node.pos_end: 错误结束
            context: 上下文，父类子类关系
            """
            return res.failure(
                RTError(
                    node.pos_start, node.pos_end,
                    "'{var_name}' is not defined".format(var_name=var_name),
                    context))
        value = value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(value)

    def visit_VarAssignNode(self, node, context):
        """
        node: 节点，提供变量名与值
        """
        # 实例化运行时
        res = RTResult()
        # 定义var_name
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))

        # 如果检测到运行时错误
        if res.error:
            # 返回运行时
            return res

        # 调用 symbol_table 类的 set 方法，将获取到的变量名设置为对应值
        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_NumberNode(self, node, context):
        return RTResult().success(
            Number(node.tok.value).set_context(context).set_pos(
                node.pos_start, node.pos_end))

    def visit_StringNode(self, node, context):
        return RTResult().success(
            String(node.tok.value).set_context(context).set_pos(
                node.pos_start, node.pos_end))

    def visit_ListNode(self, node, context):
        res = RTResult()
        elements = []

        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context)))
            if res.error:
                return res

        return res.success(
            List(elements).set_context(context).set_pos(
                node.pos_start, node.pos_end))

    def visit_BinOpNode(self, node, context):
        # 实例化运行时
        res = RTResult()
        # 获取左边节点
        left = res.register(self.visit(node.left_node, context))
        if res.error:
            return res
        # 获取右边节点
        right = res.register(self.visit(node.right_node, context))
        if res.error:
            return res

        # 如果运算Token为TT_PLUS(+)
        if node.op_tok.type == TT_PLUS:
            # result 和 error 定义为 左侧加右侧
            result, error = left.added_to(right)
        # 如果运算Token为TT_MINUS(-)
        elif node.op_tok.type == TT_MINUS:
            # result 和 error 定义为 左侧减右侧
            result, error = left.subbed_by(right)
        # 如果运算Token为TT_MUL(*)
        elif node.op_tok.type == TT_MUL:
            # result 和 error 定义为 左侧乘右侧
            result, error = left.multed_by(right)
        # 如果运算Token为TT_DIV(/)
        elif node.op_tok.type == TT_DIV:
            # result 和 error 定义为 左侧减右侧
            result, error = left.dived_by(right)
        elif node.op_tok.type == TT_POW:
            result, error = left.powed_by(right)
        elif node.op_tok.type == TT_EE:
            result, error = left.get_comparison_eq(right)
        elif node.op_tok.type == TT_NE:
            result, error = left.get_comparison_ne(right)
        elif node.op_tok.type == TT_LT:
            result, error = left.get_comparison_lt(right)
        elif node.op_tok.type == TT_GT:
            result, error = left.get_comparison_gt(right)
        elif node.op_tok.type == TT_LTE:
            result, error = left.get_comparison_lte(right)
        elif node.op_tok.type == TT_GTE:
            result, error = left.get_comparison_gte(right)
        elif node.op_tok.matches(TT_KEYWORD, 'and'):
            result, error = left.anded_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'or'):
            result, error = left.ored_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error:
            return res

        error = None
        if node.op_tok.type == TT_MINUS:
            number, error = number.multed_by(Number(-1))
        elif node.op_tok.matches(TT_KEYWORD, 'not'):
            number, error = number.notted()
        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))

    def visit_IFNode(self, node, context):
        res = RTResult()

        for condition, expr in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.error:
                return res

            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.error:
                    return res
                return res.success(expr_value)

        if node.else_case:
            else_value = res.register(self.visit(node.else_case, context))
            if res.error:
                return res
            return res.success(else_value)
        return res.success(None)

    def visit_ForNode(self, node, context):
        res = RTResult()
        elements = []

        start_value = res.register(self.visit(node.start_value_node, context))
        if res.error:
            return res

        end_value = res.register(self.visit(node.end_value_node, context))
        if res.error:
            return res

        if node.step_value_node:
            step_value = res.register(self.visit(node.step_value_node,
                                                 context))
            if res.error:
                return res
        else:
            step_value = Number(1)

        i = start_value.value

        if step_value.value >= 0:
            condition = lambda: i < end_value.value
        else:
            condition = lambda: i > end_value.value

        while condition():
            context.symbol_table.set(node.var_name_tok.value, Number(i))
            i += step_value.value

            elements.append(res.register(self.visit(node.body_node, context)))
            if res.error:
                return res

        return res.success(
            List(elements).set_context(context).set_pos(
                node.pos_start, node.pos_end))

    def visit_WhileNode(self, node, context):
        res = RTResult()
        elements = []

        while True:
            condition = res.register(self.visit(node.condition_node, context))

            if res.error:
                return res

            if not condition.is_true():
                break

            elements.append(res.register(self.visit(node.body_node, context)))
            if res.error:
                return res

        return res.success(
            List(elements).set_context(context).set_pos(
                node.pos_start, node.pos_end))

    def visit_FuncDefNode(self, node, context):
        res = RTResult()

        func_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_toks]
        func_value = Function(func_name, body_node,
                              arg_names).set_context(context).set_pos(
                                  node.pos_start, node.pos_end)

        if node.var_name_tok:
            context.symbol_table.set(func_name, func_value)

        return res.success(func_value)

    def visit_CallNode(self, node, context):
        res = RTResult()
        args = []

        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.error:
            return res
        value_to_call = value_to_call.copy().set_pos(node.pos_start,
                                                     node.pos_end)

        for arg_node in node.arg_nodes:
            args.append(res.register(self.visit(arg_node, context)))
            if res.error:
                return res

        return_value = res.register(value_to_call.execute(args))
        if res.error:
            return res
        if return_value:
            return_value = return_value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
            return res.success(return_value)
        else:
            return res.success(None)
