operators = {"^":4,"+":2, "-":2, "*":3, "/":3}
right_associative = {"^"}

def evaluate(postfix_expr):
    A = int(input("Enter number for A:"))
    B = int(input("Enter number for B:"))
    C = int(input("Enter number for C:"))
    numbers = {"A":A, "B":B, "C":C}
    Stack = []
    postfix_expr = postfix_expr.split()
    for token in postfix_expr:
        if token not in operators:
            if token in numbers:
                Stack.append(numbers[token])
            else:
                Stack.append(token)
        else:
            if len(Stack) >= 2:
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
    if len(Stack) > 1:
        print("invalid expression")
        return None 
    return Stack[0]


def infix_to_postfix(infix):
    postfix = ""
    stack = []

    for token in infix:
        if token not in operators and token != "(" and token != ")":
            postfix += token + " "
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while len(stack) > 0 and stack[-1] != "(":
                postfix += stack.pop() + " "
            if len(stack) > 0 and stack[-1] == ")":
                return ""
            else:
                stack.pop()
        else:
            while len(stack) > 0 and stack[-1] != "(" and (operators[stack[-1]] > operators[token] or (operators[stack[-1]] == operators[token] and token not in right_associative)):
                postfix += stack.pop() + " "
            stack.append(token)
    while len(stack) > 0:
        postfix += stack.pop() + " "
    return postfix
             



infix_expr = input().split()
post_fix = infix_to_postfix(infix_expr)
if post_fix == "":
    print("Not valid")
else:
    result =  evaluate(post_fix)
    if result:
        print(result)

