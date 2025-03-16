def generate_parens(n):
    res = set()
    return sorted(list(generate_parens_r(n, res)))

def generate_parens_r(n, res):
    if n == 0:
        return {}
    if n == 1:
        return {'()'}
    else:
        parens_n = generate_parens_r(n-1, res)
        prefix = set()
        infix = set()
        postfix = set()
        for parens in parens_n:
            prefix.add(f'(){parens}')
            infix.add(f'({parens})')
            postfix.add(f'{parens}()')
        return prefix.union(infix).union(postfix)

print(generate_parens(3))