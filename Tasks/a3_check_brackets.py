def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    count, i = 0, 0
    while count >= 0 and i < len(brackets_row):
        if brackets_row[i] == '(':
            count += 1
        if brackets_row[i] == ')':
            count -= 1
        i += 1
    return not bool(count)


if __name__ == '__main__':
    for row in ["", "()", "()()(()())", "(", ")", ")("]:
        print(check_brackets(row))
