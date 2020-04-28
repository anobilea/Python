import uuid
import typefy

class Evaluator:
    """receives a list with expressions (list of tokens), process this list and evaluate each one"""

    '''Store variables after they have been calculated'''
    __variables = dict()

    '''ordered list with list of tuples (var, expression) before transforming into postfix'''
    _expressions = []
    _postfix_expression = []

    def __init__(self, expression_list):
        for r in expression_list:
            self._pre_process(r)

    @staticmethod
    def raw_to_typed_expression(tokens):
        t_list = list()

        for t in tokens:
            t_list.append(typefy.BaseType.create(t))

        return t_list



    '''separate expression into var being assigned and expression'''
    def _pre_process(self, raw_expression):
        exp = []

        if '=' in raw_expression and raw_expression[1] == '=':
            exp[:] = raw_expression[2:]
            var = raw_expression[0]
        else:
            exp = raw_expression
            var = "tmp_" + uuid.uuid4().hex

        self._expressions.append((var, self.raw_to_typed_expression(exp)))


    def to_postfix(self):
        for e in self._expressions:
            self._postfix_expression.append(self._shunting_yard(e[1]))

    def _shunting_yard(self, t_token):
        pf_list = list()
        ope_stack = list()

        for t_tk in t_token:
            if t_tk.token_type == typefy.TokenTypes.INT or t_tk.token_type == typefy.TokenTypes.FLOAT or t_tk.token_type == typefy.TokenTypes.VARIABLE:
                pf_list.append(t_tk)
            elif t_tk.token_type == typefy.TokenTypes.OPERATOR:
                if len(ope_stack) == 0:
                    ope_stack.append(t_tk)
                    continue
                elif ope_stack[-1].value == '(':
                    ope_stack.append(t_tk)
                    continue
                elif t_tk.value == ')':
                    while len(ope_stack) > 0 and ope_stack[-1].value != '(':
                        pf_list.append(ope_stack.pop())
                    ope_stack.pop()
                    continue

                while len(ope_stack) > 0 and t_tk.precedence <= ope_stack[-1].precedence and ope_stack[-1].value != '(':
                    pf_list.append(ope_stack.pop())
                ope_stack.append(t_tk)

        ope_stack.reverse()
        pf_list += ope_stack
        return pf_list

    def run(self):
        self.to_postfix()

        for s in self._postfix_expression:
            text = ''
            for t in s:
                text += str(t.value)
            print(text)

