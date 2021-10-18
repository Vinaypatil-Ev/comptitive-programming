
#evaluate postifix expression using stack
def op(x, y, o):
    if o == "+":
        return x + y
    if o == "-":
        return x - y
    if o == "*":
        return x * y
    if o == "/":
        return int(x/y)
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
        if i == "+" or i == "-" or i == "*" or i == "/":
            if len(stack) >= 2:
                y = stack.pop()
                x = stack.pop()
                print(stack, "pop", "x=",x, "y=",y, i)
                z = op(x, y, i)
                stack.append(z)
                print(stack, "op", i, z, "ans")
        else:
            stack.append(int(i))
            print(stack, "add", i)
            
        # print(stack)
    return stack.pop()   
            
            


if __name__ == "__main__":
    # exp = "235*+43*-7+"
    exp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    x = evaluate_postfix(exp)
    print(x)