import pdb #import debugger


def add_numbers(a, b):
    pdb.set_trace() #set breakpoint
    result = a + b
    return result
print(add_numbers(3, 4))