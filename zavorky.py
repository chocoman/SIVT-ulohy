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
    '[]()', # true
    '({()()(()))', # false
    '({()()(())})', # true
    '(<>)', # true
    '((()())(()())())', # true
]

for pair in inputs:
    input = pair[0]
    correct_answer = pair[1]
    answer = checkParentheses(input)
    print(f'{input}, {answer}, {correct_answer}')

for (input, correct_answer) in inputs:
    answer = checkParentheses(input)
    print(f'{input}, {answer}, {correct_answer}')

