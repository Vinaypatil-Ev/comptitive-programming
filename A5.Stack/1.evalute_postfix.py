
#evaluate postifix expression using stack
def op(x, y, o):
    if o == "+":
        return x + y
    if o == "-":
        return x - y
    if o == "*":
        return x * y
    if o == "/":
        return x / y
    if o == "^":
        return x ** y
    
def evaluate_postfix(exp):
    """
        evaluate; 2 + 3*5 - 4*3 + 7
        = 2 + 3*5 - 4*3 + 7
        = 2 + 15 - 12 + 7
        = 17 - 12 + 7
        = 5 + 7
        = 12
    """
    stack = []
    for i in exp:
        if str(i).isnumeric():
            stack.append(int(i))
        else:
            if len(stack) >= 2:
                y = stack.pop()
                x = stack.pop()
                z = op(x, y, i)
                stack.append(z)
    return stack.pop()   
            
            


if __name__ == "__main__":
    exp = "235*+43*-7+"
    x = evaluate_postfix(exp)
    print(x)