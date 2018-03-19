'''
@show_args 
def do_nothing(x, y):
    pass
    
do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines): 
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''


def show_args(fn):

    def wrapper(*args, **kwargs):
        print(f"Here are the args: {args}")
        print(f"Here are the kwargs: {kwargs}")
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    pass


do_nothing(1, 2, 3, a="hi", b="bye")
