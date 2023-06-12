def calculate (expression):
    print("Calculating")
    try:
        if "+"  in expression:
            operands = expression.split(" + ")
            print(float(operands[0]) + float(operands[1]))
        elif "-" in expression:
            operands = expression.split(" - ")
            print(float(operands[0]) - float(operands[1]))
        elif "*" in expression:
            operands = expression.split(" * ")
            print(float(operands[0]) * float(operands[1]))
        elif "/" in expression:
            operands = expression.split(" / ")
            print(float(operands[0]) / float(operands[1]))
    except Exception as e:
        print(e)
exp=input("Enter expression")
calculate(exp)