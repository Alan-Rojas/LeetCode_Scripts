def valid_parentheses(array): 
    bracket_0_count, bracket_1_count, bracket_2_count = 0,0,0

    for i in array: # First I iterate trough the elements
        if i == "(": 
            bracket_0_count += 1

        elif i == "{": 
            bracket_1_count += 1

        elif i == "[": 
            bracket_2_count += 1

        elif i == ")": 
            bracket_0_count -= 1

        elif i == "}": 
            bracket_1_count -= 1

        elif i=="]":
            bracket_2_count -= 1

        if (bracket_0_count < 0) or (bracket_1_count < 0) or (bracket_2_count < 0):
            return False # It's not closed, a closing parentheses was put before.
    
    if (bracket_0_count == 0) and (bracket_1_count == 0) and (bracket_2_count == 0):
        return True
    else: 
        return False


# Let's try: 
tests = ["()", "([{}]", "[[[[]]]]", "{(()}"]
for test in tests:
    print(f"Test: {test}: {valid_parentheses(test)}")