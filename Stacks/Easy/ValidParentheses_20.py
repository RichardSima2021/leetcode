def isValid(s):
    stack = []

    open_p = {'(', '[', '{'}
    close_p = {')', ']', '}'}
    valid_pairs = {'()', '[]', '{}'}

    if len(s) == 0:
        return True
    elif len(s) == 1:
        return False

    for paren in s:
        if paren in open_p:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            elif f'{stack[-1]}{paren}' in valid_pairs:
                stack.pop(-1)
            else:
                return False

    return len(stack) == 0

