class Calculator:
    def add(self, a , b):
        return a+b
    def sub(self, a , b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a , b):
        return a/b
    def mod(self, a, b):
        return a%b
calculator = Calculator()
user_input = input("enter an expression:" )
operands = user_input.split()
operand1 = float(operands[0])
operator = operands[1]
operand2 = float(operands[2])
if operator == '+':
    result = calculator.add(operand1, operand2)
elif operator == '-':
    result = calculator.sub(operand1, operand2)
elif operator == '*':
    result = calculator.mul(operand1, operand2)
elif operator == '/':
    result = calculator.div(operand1, operand2)
elif operator == '%':
    result = calculator.mod(operand1, operand2)
else:
    result = "Invadlid operator"
print("result:", result)


        

   
    
                     
    
    

    
    