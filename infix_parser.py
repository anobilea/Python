import re
import uuid
import evaluator

def validateVarName(name):

    is_var_pattern = r"^[a-zA-Z_]+[\w]*"
    return True if re.fullmatch(is_var_pattern, name) else False


def tokenizer(expression):
    exp_pattern = '([0-9]+\.[0-9]+[eE][+-]?[0-9]+)|([0-9]+\.[0-9]+)|([0-9]+[eE][0-9]+)|([0-9]+)|([\+\-\*\/\=\(\)\=])|([\w]+)?'
    tk_lst = []
    result = re.findall(exp_pattern, expression)

    for matches in result:
        tk_lst += [tokens for tokens in matches if tokens != '']

    if '=' in tk_lst:
        if tk_lst[1] != '=' or validateVarName(tk_lst[0]) == False:
            err = 'The expression {0} cannot be evaluated'.format(expression)
            raise SyntaxError(err)

    return tk_lst


tk_list = [tokenizer('A*(B+C)'), tokenizer("b = A * ( B + C * D ) + E")]

calc = evaluator.Evaluator(tk_list)
calc.run()






























