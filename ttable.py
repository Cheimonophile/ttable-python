#!/usr/bin/python3
import sys
from fns import *

# get variables
equation = sys.argv[1].replace(' ','').replace("\\","")
print(equation)
(out,expression) = equation.split('=')
vars = sorted(set(expression).difference({'(',')','\'','+','*','\\'}))

# print header
for var in vars:
    print(var, end=',\t')
print(out)

# create stacks
var_stack = []
op_stack = []

# get every var mapping
for map in var_maps(vars):

    expr = expression

    # print the values of the vars and substitute in the equation
    for var in vars:
        print(map[var],end=',\t')
        expr = expr.replace(var,str(map[var]))
    
    # substitute every variable in the equ
    print(expr)

    
    print()


print(expression)