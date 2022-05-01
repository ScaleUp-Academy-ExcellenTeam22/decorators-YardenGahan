from functools import wraps


class typeIncorrectError(ValueError):
    """Raised when the input value is too small"""
    pass


def func1(int):
    pass


@func1
def decorator(type_to_check):
    @wraps(type_to_check)
    def wrapper(func):
        if type(func) == type_to_check:
            print("its the correct type")
        else:
            raise typeIncorrectError

    return wrapper
