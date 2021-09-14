allowed_signs = ['+', '-']

math_expresion = input("Enter your math expresion: ")
try:
    for cur_index in range(0, len(math_expresion) - 1):
        if (math_expresion[cur_index] in allowed_signs) and (math_expresion[cur_index + 1] in allowed_signs):
            raise ValueError
    print(True, '\b,', eval(math_expresion))
except (ValueError, NameError, SyntaxError):
    print(False, '\b,', None)
