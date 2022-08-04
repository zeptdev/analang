#!/usr/bin/env python3

import os
import sys
import subprocess
from collections import *

stack = deque()

OP_PUSH = 0
OP_PLUS = 1
OP_MINUS = 2
OP_WRITE = 3
COUNT_OPS = 4

def push(x):
    return (OP_PUSH, x)
def plus():
    return (OP_PLUS, )
def write():
    return (OP_WRITE, )
program = "5 6 + write".split()
""" program = [
    push(34),
    push(35),
    plus(),
    write()
] """ 
def com(program):
    ip = 0
    for ip in range(len(program)):
        assert COUNT_OPS == 4, "You have instructions not handled properly."
        code = program[ip]
        if code == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif code == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif code == 'write':
            a = stack.pop()
            print(a)
        else:
            stack.append(int(code))
        ip += 1
def sim(program):
    for op in program:
        print("The Stack: " + str(stack))
        if op[0] == OP_PUSH:
            stack.append(int(op[1]))
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_WRITE:
            a = stack.pop()
            print(a)

com(program)
