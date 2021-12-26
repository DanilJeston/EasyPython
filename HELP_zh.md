#### 使用教程
运算:
    使用: <整数型/浮点型/变量...> +, -, *, /, ^ <整数型/浮点型/变量...>
    效果: 对多个数进行数学运算
    例子: 
        >>> 9 * 9
            81
        >>> 5 + 7
            12
        >>> 10 - 10
            0


变量:
    使用: define <变量名> = <True/False/整数型/浮点型...> or define <变量名> = <if语句>
    效果: 将一个值储存到变量中
    例子: 
        >>> define age = 18
        >>> define x = define y = define z = 9
        >>> define x = age * y

逻辑判断:
    使用: <True/False/整数型/浮点型/变量...> ==, !=, <, >, <=, >= <True/False/整数型/浮点型/变量...>
    效果: 对比并返回True或False 
    例子:
        >>> 1 == 1 and 2 == 2
            True
        >>> 1 > 2 or 3 < 4
            True

if 语句:
    else:
        使用: if <逻辑判断> then <返回值> else <返回值>
        效果: 判断如果条件符合返回对应值，否则返回对应值
    elif:
        使用: if <逻辑判断> then <返回值> elif <逻辑判断> then <返回值> ...
        效果: 判断，当如果条件一满足返回对应值，不满足则看条件二是否满足...
    注: elif与else可混搭使用。
    例子:
        >>> if 18 > 20 then 2 else 1
            1
        >>> if 18 > 20 and 19 > 21 then 2 elif 18 < 20 and 17 < 18 then 1
            1