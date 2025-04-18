from ..sprites import Sprite
from ..utils import parseAnimation
import pygame

class Animation(Sprite):
    def __init__(self, name: str, fps: int = 24):
        self.Animations, self.CurAnim = parseAnimation(name)
        self.CurIndex = 0
        self.FPS = fps
        self._Cur = 0
        self.Complete = False
        self.Paused = False
        self.Looped = False

        super().__init__(self.CurImage["Image"])
        self.sizeOffset = pygame.math.Vector2(0, 0)
        self.posOffset = pygame.math.Vector2(0, 0)

    @property
    def CurImage(self):
        return self.Animations[self.CurAnim][self.CurIndex]

    def animUpdate(self):
        if self.Complete and not self.Paused: return
        if self.Paused: return
        if self._Cur >= 1 / self.FPS:
            self._Cur = 0
            self.CurIndex += 1
            if self.CurIndex >= len(list(self.Animations[self.CurAnim].keys())):
                self.CurIndex = 0
            self.image = self.CurImage["Image"].convert_alpha()
            self.size = pygame.math.Vector2(self.CurImage["Image"].get_size()) + self.sizeOffset

        self._Cur += self.Engine.Runtime.getTime() / 1000

    def playAnim(self, name: str, loop: bool = False):
        self.CurIndex = 0
        self.CurAnim = name
        self.Complete = False
        self.Looped = loop
        self.Paused = False
        self._Cur = 0

    def runAnim(self):
        self.Looped = True
        self.Complete = False
        self.Paused = False


class VectorAnimation(Animation):
    def __init__(self, name: str, fps: int = 24):
        super().__init__(name, fps)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)



