# simple reverse notation of arithmetic expressions

# Always go for stack
# insert numbers until we hit an operator, then we pop 2 last numbers for that operand


# assume only integers for the numericals
# assume only arithmetic operations e.g. no sqrt, log etc
postfix = ['2', '1', '+', '3', '*']

# let's utilize python3 string formatter for ease of implemeting arithmetic operator evaluation
def compute_postfix(notation):
    stack = []
    for c in postfix:
        if c.isnumeric():
            stack.append(c)
        else:
            arg0 = stack.pop()
            arg1 = stack.pop()
            stack.append(eval(f'{arg0}{c}{arg1}'))
    return stack[0]

print(compute_postfix(postfix))

