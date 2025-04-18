from engineV3 import Base, Engine
from pygame import gfxdraw, Vector2, Rect, math, geometry
import pygame


class Circle(Base, geometry.Circle):
    def __init__(self, pos, radius, color):
        Base.__init__(self)

        self.pos = pos
        self.size = Vector2(1, 1)
        self.size.scale_to_length(radius)
        self.color = color
        geometry.Circle.__init__(self, pos.x, pos.y, self.size.length())

    def draw(self):
        gfxdraw.circle(self.Engine.Screen, int(self.pos.x), int(self.pos.y), int(self.size.length()), self.color)

class Rectangle(Base):
    def __init__(self, rect, color):
        super().__init__()
        self.pos =  Vector2(rect.topleft)
        self.Color = color
        self.size = Vector2(rect.size)

    def draw(self):
        gfxdraw.rectangle(self.Engine.Screen, Rect(self.pos, self.size), self.Color)

