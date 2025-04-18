from websockets.headers import parse_extension_item

from .engine import Base
from copy import copy

def getDifference(x1, x2):
    return x2 - x1

def getVec2Difference(vec1, vec2):
    return vec2 - vec1

class TweenGroup(Base, list):
    def __init__(self):
        Base.__init__(self)
        list.__init__(self)

    def update(self):

        for tween in self[:]:
            instances = {}

            for propertyName, propertyValue in tween.Properties.items():
                if instances.get(propertyName, None) is None:
                    instances[propertyName] = copy(tween.Object.__dict__[propertyName])
                    if propertyValue == instances.get(propertyName, None):
                        instances[propertyName] = tween.Object.__dict__[propertyName].__copy__() if not isinstance(tween.Object.__dict__[propertyName], int | float | str | bool) else tween.Object.__dict__[propertyName]
                tween.Object.__dict__[propertyName] = instances[propertyName] + (tween.tweenFunc(tween.CurTime / tween.Time) * (propertyValue - instances[propertyName]))

            if tween.CurTime == tween.Time:
                if tween.onComplete is not None:
                    tween.onComplete()
                self.remove(tween)
                continue

            tween.CurTime += self.Engine.Runtime.getTime() / 1000

            if tween.CurTime > tween.Time:
                tween.CurTime = tween.Time