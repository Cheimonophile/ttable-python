# adds two values
def add(a,b):
    if a == '1' and b == '1':
        return '1'
    else:
        return '0'

# multplies two values
def mult(a,b):
    if a=='1' or b=='1':
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

# evaluates the expression
