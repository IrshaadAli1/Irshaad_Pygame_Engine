from typing import Callable

class Function:
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class SetFunction(Function):
    def __init__(self, func: Callable, *args, **kwargs):
        super().__init__(func)
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return self.func(*self.args, **self.kwargs)
