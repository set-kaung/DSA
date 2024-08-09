# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

Stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        Stack.append(float(token))
    else:
        right = Stack.pop()
        left = Stack.pop()
        result = 0
        if token == "+":
            result = float(left) + float(right)
        elif token == "-":
            result = float(left) - float(right)
        elif token == "*":
            result = float(left) *float(right)
        elif token == "/":
            result = float(left) / float(right)
        elif token == "%":
            result = float(left) % float(right)
        elif token == "^":
            result = float(left) ** float(right)
        Stack.append(result)

        
print('%.1f' % Stack[0])


        
