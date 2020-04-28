import re
import uuid
import evaluator

def validateVarName(name):

    is_var_pattern = r"^[a-zA-Z_]+[\w]*"
    return True if re.fullmatch(is_var_pattern, name) else False


def tokenizer(expression):
    exp_pattern = '([0-9]+\.[0-9]+[eE][+-]?[0-9]+)|([0-9]+\.[0-9]+)|([0-9]+[eE][0-9]+)|([0-9]+)|([\+\-\*\/\^\=\(\)\=])|([\w]+)?'
    tk_lst = []
    result = re.findall(exp_pattern, expression)

    for matches in result:
        tk_lst += [tokens for tokens in matches if tokens != '']

    if '=' in tk_lst:
        if tk_lst[1] != '=' or validateVarName(tk_lst[0]) == False:
            err = 'The expression {0} cannot be evaluated'.format(expression)
            raise SyntaxError(err)

    return tk_lst


e1 = "a = 8 / 4^2 * 3.14"
e2 = "b = a * a / (a * 1.5)"
e3 = "d=10"
e4 = "e = a + b - 4 ^ 0.5 + d"
e5 = "d * (10 / (3 + 2))"
e6 = "f=-10"

#tk_list = [tokenizer(e1), tokenizer(e2), tokenizer(e3), tokenizer(e4), tokenizer(e5), tokenizer(e6)]
tk_list = [tokenizer(e6)]

calc = evaluator.Evaluator(tk_list)
result = calc.run()

for v, r in result.items():
    print(f"{v} = {r}")






























