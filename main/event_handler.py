from .function_database import SetFunction, Function
import pygame

class EventHandler(dict):
    def __init__(self):
        super(EventHandler, self).__init__({
            "Regular": {pygame.WINDOWCLOSE: SetFunction(quit)},
            "EventSent": {},
            "KeyDown": {pygame.K_ESCAPE: SetFunction(quit)},
            "KeyUp": {},
        })

    def insertRegularEvent(self, event: int, func: SetFunction):
        self["Regular"][event] = func

    def insertKeyDownEvent(self, event: int, func: SetFunction):
        self["KeyDown"][event] = func

    def insertKeyUpEvent(self, event: int, func: SetFunction):
        self["KeyUp"][event] = func

    def insertEventSentEvent(self, event: int, func: Function):
        self["EventSent"][event] = func

    def runEvents(self):
        for event in pygame.event.get():
            if self["Regular"].get(event.type, None) is not None: self["Regular"][event.type]()
            if self["EventSent"].get(event.type, None) is not None: self["EventSent"][event.type](event)

            if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP: return

            if self["KeyDown"].get(event.key, None) is not None: self["KeyDown"][event.key]()
            if self["KeyUp"].get(event.key, None) is not None: self["KeyUp"][event.key]()
