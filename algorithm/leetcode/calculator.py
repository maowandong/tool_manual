#!/usr/bin/env python
# coding=utf-8

class Solution_224:
    """
    题目：
        实现一个基本的计算器来计算一个简单的字符串表达式的值。
        字符串表达式可以包含左括号(，右括号)，加号+，减号-，非负整数和空格 。
    解法：（栈）
        遇到'('将之前计算的结果和括号前的符号压入栈，遇到')'将栈中的结果和符号弹出栈
    """

    def calculate(self,s : str) -> int:
        """

        :param s:
        :return:
        """

        stack = []
        l, r = 0, 0
        op = 1

        for c in s:
            # 根据位数累加得到数字
            if c.isdigit():
                r = r * 10 + int(c)
            elif c in '+-':
                l += r * op
                r, op = 0, 1 if c == '+' else -1
            elif c == '(':
                stack.append(l)
                stack.append(op)
                op, l = 1, 0
            elif c == ')':
                l += r * op
                r = 0
                l = stack.pop() * l + stack.pop()

        # ')' 右括号后再跟加减操作，需要再进行操作
        return l + op * r

test_case = [
    '124 + 40',
    '124 - 50 + 3',
    '124 - ((50 - 43) - 20) + 1'
]

solution = Solution_224()
for case in test_case:
    print("%s = %d" % (case, solution.calculate(case)))