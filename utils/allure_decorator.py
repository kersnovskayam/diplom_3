import functools

import allure

def allure_decorator(step_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with allure.step(step_name):
                return func(*args, **kwargs)
        return wrapper
    return decorator
