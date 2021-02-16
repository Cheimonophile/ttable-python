#!/usr/bin/python3
import sys

# global variables
digits = {'0','1'}
ops = ('+','*')

# adds two values
def add(a,b):
    if a == '1' or b == '1':
        return '1'
    else:
        return '0'

# multplies two values
def mult(a,b):
    if a=='1' and b=='1':
        return '1'
    else: 
        return '0'

# negates a value
def neg(a):
    if a=='1':
        return '0'
    else:
        return '1'

# returns a list of maps given the number of variables
def var_maps(vars):
    maps = []
    for i in range(2**len(vars)):
        map = {}
        for var in sorted(vars,reverse=True):
            map[var] = str(i%2)
            i = i//2
        maps.append(map)
    return maps

# calculates based on a given operator
def calc(a,b,op):
    if op =='+':
        val = add(a,b)
        return val
    elif op=='*':
        val = mult(a,b)
        return val
    else:
        raise Exception("Invalid Operator")

# evaluates the expression
def eval(expr):
    
    # init stacks
    val_stack = []
    op_stack = []

    # loop over the expression
    for c in expr:
        if c in digits:
            val_stack.append(c)
        elif c == '\'':
            val_stack.append(neg(val_stack.pop()))
        elif c in ops and (len(op_stack)<1 or op_stack[-1]=='('):
            op_stack.append(c)
        elif c in ops:
            while len(op_stack)>0:
                prev_op = op_stack.pop()
                if prev_op in ops and ops.index(c) < ops.index(prev_op):
                    b = val_stack.pop()
                    a = val_stack.pop()
                    val_stack.append(calc(a,b,prev_op))
                else:
                    break
            op_stack.append(c)
        elif c =='(':
            op_stack.append(c)
        elif c ==')':
            while len(op_stack)>0:
                b = val_stack.pop()
                a = val_stack.pop()
                op = op_stack.pop()
                while op == '(':
                    op = op_stack.pop()
                val_stack.append(calc(a,b,op))
        else:
            raise Exception("Unrecognized Token: "+c)
    
    # return statement
    return val_stack[0]

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
    print(eval(expr))