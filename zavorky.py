def checkParentheses(text):
    depth = 0
    for character in text:
        if character == '(':
            depth += 1
        elif character == ')':
            depth -= 1
        if depth < 0:
            # closing paren with no matching opening paren
            return False
    if depth > 0:
        # some parens were not closed
        return False
    else:
        return True

def parensMatch(left, right):
    if (left == '(' and right == ')'):
        return True
    if (left == '{' and right == '}'):
        return True
    if (left == '<' and right == '>'):
        return True
    if (left == '[' and right == ']'):
        return True
    return False

def checkMixedParentheses(text):
    stack = []
    for character in text:
        if character in '({<[':
            stack.append(character)
        elif character in ')}>]':
            if len(stack) == 0:
                return False
            if parensMatch(stack[-1], character):
                stack.pop(-1)
    if len(stack) == 0:
        return True
    else:
        return False


inputs = [
    ('())(()', False),
    ('((()()(()))', False),
    ('((()()(())))', True),
    ('(()())', True),
    ('((()())(()())())', True),
    ('()', True),
    ('(())', True),
    ('(()()()()()())', True),
    ('((()()()()()())(()))', True),
    ('(()()()()()()))(())', False),
    ('())(()', False),
    ('(()()())', True),
    ('((()()())()())', True),
]
hard_inputs = [
    ('[]>()', False),
    ('({()()(()))', False),
    ('({()()(())})', True),
    ('(<>)', True),
    ('((()())(()())())', True),
]

for (input, correct_answer) in hard_inputs:
    answer = checkMixedParentheses(input)
    print(f'{input}, {answer}, {correct_answer}')

