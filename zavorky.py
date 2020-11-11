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

def soucet(a, b):
    c = a + b
    return c
inputs = [
    ('()', True),
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
    '[]()', # true
    '({()()(()))', # false
    '({()()(())})', # true
    '(<>)', # true
    '((()())(()())())', # true
]


for (input, correct_answer) in inputs:
    answer = checkParentheses(input)
    print(f'{input}, {answer}, {correct_answer}')

