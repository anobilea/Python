import parser
import evaluator


def calculate(expression):
    return evaluator.Evaluator([parser.tokenizer(expression)]).run()


def calculate_file(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(parser.tokenizer(line))

    return evaluator.Evaluator(lines).run()



