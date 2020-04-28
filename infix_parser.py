import re
import uuid
import evaluator

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4}
exp_symbols = ['=', '+', '-', '*', '/', '^', '(', ')']
variables = dict()


def preProcessExpression(inputExp):
    pattern = r"\s"

    exp = inputExp.split('=')
    exp_len = len(exp)

    if exp_len == 2:
        var_name = exp[0].strip()
        if not validateVarName(var_name):
            err = 'The expression {0} cannot be evaluated'.format(inputExp)
            raise SyntaxError(err)
        else:
            return [var_name, re.sub(pattern, '', exp[1])]
    elif exp_len == 1:
        return [re.sub(pattern, '', exp[0])]

    return []


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


'''
    token = ""
    tokens = list()
    for c in expression:
        if c in exp_symbols:
            if token != '':
                tokens.append(token)
            token = ""
            tokens.append(c)
        else:
            token += c

    if len(token):
        tokens.append(token)
    return tokens
'''


def shuntingYard(tokens):
    postfix_expression = list()
    ope_stack = list()

    for tk in tokens:
        if str.isnumeric(tk):
            postfix_expression.append(tk)
        elif tk in operators:
            if len(ope_stack) == 0:
                ope_stack.append(tk)
                continue
            elif ope_stack[-1] == '(':
                ope_stack.append(tk)
                continue
            ope_precedence = operators[tk]
            while len(ope_stack) > 0 and ope_precedence <= operators[ope_stack[-1]] and ope_stack[-1] != '(':
                postfix_expression.append(ope_stack.pop())
            ope_stack.append(tk)
        elif tk == ')':
            while len(ope_stack) > 0 and ope_stack[-1] != '(':
                postfix_expression.append(ope_stack.pop())
            ope_stack.pop()

    ope_stack.reverse()
    postfix_expression += ope_stack

    return postfix_expression


def postfix(token_list):
    return shuntingYard(token_list)


def process_expression(strexp):

    t_expression = tokenizer(strexp)
    exp = []
    varName = ""

    if '=' in t_expression and t_expression[1] == '=':
        exp[:] = t_expression[2:]
        varName = t_expression[0]
    else:
        exp = t_expression
        varName = "tmp_" + uuid.uuid4().hex

    postfix_exp = postfix(exp)
    variables[varName] = postfix_exp



tk_list = [tokenizer('A*(B+C)'), tokenizer("b = A * ( B + C * D ) + E")]

calc = evaluator.Evaluator(tk_list)
calc.run()






























