from ..main.function_database import SetFunction
from ..main.engine import Base


class Timer(Base, SetFunction):
    def __init__(self, delay: float, interval: float, func: SetFunction, repeat: int = 1):
        Base.__init__(self)
        SetFunction.__init__(self, func.func, *func.args, **func.kwargs)
        self.Delay = delay
        self.Interval = interval
        self.Repeat = repeat

        self.CurTime = 0
        self.Delayed = False

        self.Paused = False


    def update(self):
        if self.Paused: return
        if not self.Delayed and self.CurTime > self.Delay:
            self.Delayed = True
            self.CurTime = 0
        elif self.Delayed and self.CurTime > self.Interval and self.Repeat >= 1:
            self()
            self.CurTime = 0
            self.Repeat -= 1
        self.CurTime += self.Engine.Runtime.getTime() / 1000



