import pygame

class Engine:
    _Engine = None

    def __new__(cls, *args, **kwargs):
        if cls._Engine is None:
            cls._Engine = super(Engine, cls).__new__(cls)
        return cls._Engine

    @classmethod
    def getEngine(cls):
        if cls._Engine is None:
            return cls.__new__(cls)
        return cls._Engine

    def __init__(self):
        self.Init = pygame.init()
        self.Window = pygame.window.Window()
        self.Window.get_surface()

        self.BGColor = (0, 0, 0)
        self.Active = True

        from .input import Input
        self.Input = Input()

        from .runtime import Runtime
        self.Runtime = Runtime()

        from .states import States
        self.States = States()

        from .event_handler import EventHandler
        self.Events = EventHandler()

        from .tween_handler import TweenGroup
        self.Tween = TweenGroup()

        from .timer_handler import TimerGroup, Sequence
        self.Timer = TimerGroup()
        self.Sequence = Sequence()

        from .mouse import Mouse
        self.Mouse = Mouse()

        from .camera import Camera
        self.Cameras = []
        self.Sprites = []
        self._MainCamera = Camera(0, 0, 0, 0)

    def updateUpdate(self):
        self.Events.runEvents()
        self.Tween.update()
        self.Timer.update()
        self.Sequence.update()
        self.Input.update()
        self.Mouse.update()

    def drawUpdate(self):
        self._MainCamera.Rect = pygame.FRect(0, 0, self.Size.x, self.Size.y)
        for cam in self.Cameras:
            cam.render(self.Sprites)

    def update(self):
        self.Screen.fill(self.BGColor)
        self.States.runCurState()
        self.updateUpdate()
        self.drawUpdate()
        self.postUpdate()

    def postUpdate(self):
        self.Runtime.tick()
        self.Window.flip()

    def run(self):
        while self.Active:
            self.update()

    @property
    def mainState(self):
        return self.States.getState("Main")

    @mainState.setter
    def mainState(self, value):
        self.States.setState("Main", value)

    @property
    def Screen(self):
        return self.Window.get_surface()

    @property
    def Size(self):
        return pygame.Vector2(self.Screen.get_size())

    @property
    def MainCamera(self):
        return self._MainCamera



class Base:
    def __init__(self):
        self.Engine = Engine.getEngine()