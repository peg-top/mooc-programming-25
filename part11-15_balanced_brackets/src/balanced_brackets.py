def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    # Найти первую закрывающую скобку
    for i, char in enumerate(my_string):
        if char in ")]":
            # Проверяем, совпадает ли скобка с предыдущей
            if i > 0 and ((char == ')' and my_string[i-1] == '(') or (char == ']' and my_string[i-1] == '[')):
                # Убираем эти две скобки и проверяем оставшуюся строку
                new_string = my_string[:i-1] + my_string[i+1:]
                return balanced_brackets(new_string)
            else:
                return False

if __name__ == "__main__":

    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)