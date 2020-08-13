#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 16:02
# @Author  : YaoJa


def Fib(n):
    return 1 if n <= 2 else Fib(n-1) + Fib(n-2)


a = int(input("请输入斐波那契数："))

print(Fib(a))

