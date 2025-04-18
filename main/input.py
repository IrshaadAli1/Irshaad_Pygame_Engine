from .engine import Base
import pygame

def keyPressed(_type=any, *keys):
    return _type([pygame.key.get_pressed()[pygame.key.key_code(x)] for x in keys])


class Key:
    def __init__(self):
        self.Pressed = False
        self.Held = False
        self.Released = False

        self.HoldTime = 0
        self.LastHeldTime = 0

    def __str__(self):
        return f"<class Key>(Pressed: {self.Pressed}; Held: {self.Held}; Released: {self.Released}; HoldTime: {self.HoldTime}; LastHeldTime: {self.LastHeldTime})"


class Input(Base, dict):
    def __init__(self):
        Base.__init__(self)
        dict.__init__(self)

        [self.__setitem__(z, Key()) for z in [getattr(pygame.constants, x) for x in list(filter(lambda x: x.startswith("K_"), dir(pygame.constants)))]]

    def update(self):
        for i in self.keys():
            currentKey: Key = self[i]
            if currentKey.Held:
                currentKey.HoldTime += self.Engine.Runtime.getTime() / 1000

            if pygame.key.get_pressed()[i]:
                if currentKey.HoldTime > 0:
                    currentKey.Pressed = False
                else:
                    currentKey.Pressed = True
                currentKey.Held = True
            else:
                currentKey.Held = False
                if currentKey.HoldTime > 0:
                    currentKey.Released = True
                else:
                    currentKey.Released = False
                currentKey.LastHeldTime = currentKey.HoldTime
                currentKey.HoldTime = 0


    def __getitem__(self, item: str | int | float | tuple | list):
        if isinstance(item, str):
            return self.__getitem__(pygame.key.key_code(item))

        if isinstance(item, int | float):
            return dict.__getitem__(self, item)

        if isinstance(item, tuple | list):
            data = Key()
            if item[0] == any:


                for key in data.__dict__.keys():
                    if isinstance(data.__dict__[key], bool):
                        data.__dict__[key] = any([self[x].__dict__[key] for x in item[1::]])
                    if isinstance(data.__dict__[key], int | float):
                        data.__dict__[key] = max([self[x].__dict__[key] for x in item[1::]])

            elif item[0] == all:
                for key in data.__dict__.keys():
                    if isinstance(data.__dict__[key], bool):
                        data.__dict__[key] = all([self[x].__dict__[key] for x in item[1::]])
                    if isinstance(data.__dict__[key], int | float):
                        data.__dict__[key] = min([self[x].__dict__[key] for x in item[1::]]) if all(self[x].Pressed | self[x].Held for x in item[1::]) else 0

            else:
                for key in data.__dict__.keys():
                    if isinstance(data.__dict__[key], bool):
                        data.__dict__[key] = any([self[x].__dict__[key] for x in item[:]])
                    if isinstance(data.__dict__[key], int | float):
                        data.__dict__[key] = max([self[x].__dict__[key] for x in item[:]])

            return data