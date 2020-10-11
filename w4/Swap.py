def swap(values):
    def wrapper(*args, **kwargs):
        args = reversed(args)
        values(*args, **kwargs)
    return wrapper


@swap
def div(x, y, show = False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show = True)
