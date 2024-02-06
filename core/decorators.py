def handle_none_argument(func):
    def wrapper(self, *args, **kwargs):
        for arg in args:
            if arg is None:
                return
        for key, value in kwargs.items():
            if value is None:
                return
        return func(self, *args, **kwargs)
    return wrapper
