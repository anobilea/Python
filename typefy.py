import re
from enum import IntFlag


class TokenTypes(IntFlag):
    OPERAND_MASK = 0b001
    INT = 3
    FLOAT = 5
    OPERATOR = 4
    VARIABLE = 7
    NONE = 8


class BaseType:

    value = None
    token_type = TokenTypes.NONE

    @staticmethod
    def is_int(v: str):
        i_number = 0
        result = True
        try:
            i_number = int(v)
        except ValueError:
            result = False
        return result, i_number

    @staticmethod
    def is_float(val: str):
        f_number = 0.0
        result = True
        try:
            f_number = float(val)
        except ValueError:
            result = False
        return result, f_number

    @staticmethod
    def is_variable(val: str):
        is_var_pattern = r"^[a-zA-Z_]+[\w]*"
        return True if re.fullmatch(is_var_pattern, val) else False, val

    @staticmethod
    def is_operator(val: str):
        ope_regex = "^[\+\-\*\/\^\(\)]{1,1}$"
        return True if re.fullmatch(ope_regex, val) else False, val

    @staticmethod
    def create(token: str):

        result, i_value = BaseType.is_int(token)
        if result:
            return IntType(i_value)

        result, f_value = BaseType.is_float(token)
        if result:
            return FloatType(f_value)

        result, ope = BaseType.is_operator(token)
        if result:
            return OperatorType(ope)

        result, var = BaseType.is_variable(token)
        if result:
            return VarType(var)

        return None


class IntType(BaseType):

    def __init__(self, value: int):
        self.value = value
        self.token_type = TokenTypes.INT


class FloatType(BaseType):

    def __init__(self, value: float):
        self.value = value
        self.token_type = TokenTypes.FLOAT


class VarType(BaseType):

    def __init__(self, value: str):
        self.value = value
        self.token_type = TokenTypes.VARIABLE



class OperatorType(BaseType):
    _operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 4, ')': 4}

    def __init__(self, value: str):
        self.value = value
        self.token_type = TokenTypes.OPERATOR
        self.precedence = self._operators[self.value]



