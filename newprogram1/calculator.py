from typing import Any, Callable

OPERATORS = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' :  lambda x, y: x * y,
    '/' :  lambda x, y: x / y,
}

def get_user_input(message: str, typing: Any = str, validator: Callable = None, retry: bool=True) -> Any:
    """
    Gets input from a user, types it with "typing". If that typing raises an error, 
    and retry is true, will retry getting input

    Validator is any callable (function) that returns a tuple of (bool, str) where bool is true/false if
    the user's input is valid and str is any messages.
    """
    
    val = input(message)
    try:
        return_val = typing(val)
        if validator is not None:
            validation_result = validator(return_val)
            if not validation_result[0]:
                raise Exception(f"Validation failed for your input: { validation_result[1] }")
    except Exception as exc:
        print(f"Exception with your input: {exc}")
        if retry:
            return_val = get_user_input(message, typing, validator, retry)
    
    return return_val

def get_user_yes_no(message: str) -> bool:
    """
    Gets a yes or no input from a user

    Returns a boolean
    """
    def cast_yes_no(x):
        if x.lower() in ['yes', 'y']:
            return True
        if x.lower() in ['no', 'n']:
            return False
        raise Exception("Not a valid input. (Yes/y/Y or No/n/N) ")
    return get_user_input(f"{ message } (Yes/y/Y or No/n/N)", typing=cast_yes_no)


def calculator():
    """Present a basic calculator to the user"""
    print("Welecome To Calculator")
    
    first_num = get_user_input("Enter first number: ", float)
    second_num = get_user_input("Enter second number: ", float)

    def validate_operator(to_be_validated: str) -> bool:
        if to_be_validated not in OPERATORS.keys():
            return False, f"Input not in {OPERATORS.keys()}"
        return True, ""
    operator = get_user_input("Enter an operator (+, -, *, /): ", validator=validate_operator)
    
    print(f"The result of { first_num } { operator } { second_num } = { OPERATORS[operator](first_num, second_num) }")

if __name__ == "__main__":
    calculator()
    while get_user_yes_no("Would you like to do another calculation? "):
        calculator()


## todos to learn more
## * extend this program to take user input in a single line. i.e. 1 + 1 and then do the work on that
## * What happens if I try to do a bad math operation like 1 / 0 ? How could you fix that?
## * Add a few more math operations: % (modulus), & (xor), ^ (exponential/raises)
## * Could you build a new calculator that has memory? So you can do one operation, then a second on the result of that first, and so on?
## I.e. 1+ 1 = 2 + 5 = 7 * 3 = 21 on and on forever?