# Python
This project implements a basic calculator that reads an expression containint the operaneds +. -. *, / and ^.
The expression can contain variables and they automatically created in the order they appear (examples below). 
To calculate an expression, the program performs 4 steps: 

	Using regular expressions, the expression is parsed into a list of operands and operators in its original infix form.
	The infix expression is transformed into postfix using the shunting yard algorithm.
	The symbols in the postfix expressions are "typefied", strings are converted into integers, float, operator or variable types.
	The typed postfix expression is then evaluated using stack. 

The result of each line is stored in a dictionary where the key is variable name.

Example of supported expressions:

radius = 7.5
pi = 3.141592
area = pi*radius^2
p1x = -3.10e-2
p1y = 0.5
p2x = 1.317183987
p2y = 3.18
distance = (p2x - p1x)^2 + (p2y - p1y) ^ 2


