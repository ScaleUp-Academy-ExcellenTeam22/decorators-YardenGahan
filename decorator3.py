import decorator


# calls the function it wraps twice
@decorator.decorator
def decorator(func, string):
    func(string)
    func(string)
    return
