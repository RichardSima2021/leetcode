def evalRPN(tokens):
    number_stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            num2 = number_stack.pop(-1)
            num1 = number_stack.pop(-1)
            # print(f'num1: {num1}, num2: {num2}, operator:{token}')
            if token == '+':
                number_stack.append(num1+num2)
            elif token == '-':
                number_stack.append(num1-num2)
            elif token == '*':
                number_stack.append(num1*num2)
            else:
                number_stack.append(int(num1/num2))
        else:
            number_stack.append(int(token))
        # print(number_stack)
    return int(number_stack[0])


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))






