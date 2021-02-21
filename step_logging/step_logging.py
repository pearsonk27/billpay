from functools import wraps
from database import database
from messaging import email
import traceback

def log_on_call(func):
    @wraps(func)
    def wrapper(*args, **kw):
        """
        Expectations:
            - execution_log_id is an attribute of the self variable
            - self variable is the first variable of every function
            - execution_log_id is the third parameter in the __init__ funtion
        """
        execution_step_log_id = None
        if func.__name__ != "__init__":
            execution_step_log_id = database.start_execution_step(args[0].execution_log_id, func.__doc__)
        res = None
        try:
            res = func(*args, **kw)
        except Exception as ex:
            handle_error(args[0].task_name, execution_step_log_id, func.__doc__, ex)
        finally:
            if func.__name__ != "__init__":
                database.end_execution_step(execution_step_log_id)
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

def handle_error(task_name, execution_step_log_id, step_name, ex):
    """"""
    database.add_error(execution_step_log_id, ex, traceback.format_exc())
    email.send_failure_message(task_name, step_name, ex)
    raise ex
