from functools import wraps
from database import database

def log_on_call(func):
    @wraps(func)
    def wrapper(*args, **kw):
        """
        Expectations:
            - execution_log_id is an attribute of the self variable
            - self variable is the first variable of every function
            - execution_log_id is the third parameter in the __init__ funtion
        """
        if func.__name__ != "__init__":
            database.start_execution_step(args[0].execution_log_id, func.__doc__)
        res = func(*args, **kw)
        if func.__name__ != "__init__":
            database.end_execution_step(args[0].execution_log_id)
        return res
    return wrapper

def decorate_all_functions(function_decorator):
    def decorator(cls):
        for name, obj in vars(cls).items():
            if callable(obj):
                try:
                    obj = obj.__func__  # unwrap Python 2 unbound method
                except AttributeError:
                    pass  # not needed in Python 3
                setattr(cls, name, function_decorator(obj))
        return cls
    return decorator

def handle_error():
    """"""
    print("Not implemented yet")
