from ..main.function_database import SetFunction
from ..main.engine import Base
import pytweening as tweenFuncs


class Tween(Base):
    def __init__(self, tweenFunc, obj, time, properties: dict[str, any], onComplete: SetFunction = None):
        super().__init__()
        self.tweenFunc = tweenFunc
        self.Object = obj
        self.Time = time
        self.Properties = properties

        self.onComplete = onComplete
        self.CurTime = 0

    def start(self):
        self.Engine.Tween.append(self)
