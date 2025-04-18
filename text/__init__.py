from ..sprites import Sprite
from .. import utils
from typing import Callable
import pygame.freetype
import pygame
import string
pygame.font.init()

class Character(Sprite):
    def __init__(self, image, pos):
        super().__init__(image)
        self.pos = pos


class Text(list):
    def __init__(self, chars: dict[str, pygame.Surface], text: str, pos: pygame.Vector2 | tuple[float, float], size: float, charFunc: Callable = None):
        super().__init__()
        self.characterErrors = []

        self.Text = text
        self.CharData = chars
        self.Size = size
        self.Position = pos

        self.horizontalSpacing = 0
        self.verticalSpacing = 0

        self.CharFunc = charFunc

        self.clearErrorsOnRender = False

    def render(self):
        if self.clearErrorsOnRender: self.characterErrors.clear()
        self.clear()

        pos = self.Position.copy()
        fc = None
        for char in self.Text:
            if self.characterErrors.__contains__(char) and not self.clearErrorsOnRender: continue
            try:
                if char == "\n":
                    pos.x = fc.pos.x
                    pos.y = fc.pos.y + self.verticalSpacing + fc.size.y
                    fc = None
                    continue
                character = Character(self.CharData[char], pos.copy())
                character.size *= self.Size

                if fc is None:
                    fc = character

                self.append(character)
                pos.x += character.size.x + self.horizontalSpacing

            except KeyError:
                self.characterErrors.append(char)

    def draw(self):
        self.render()
        for char in self:
            if self.CharFunc:
                self.CharFunc(char)

            char.draw()

    @classmethod
    def fromPygameFont(cls, font: pygame.Font | str | pygame.freetype.Font):
        f = utils.loadFont(font)

        chars = {}
        for char in string.printable:
            chars[char] = f.render(char, True, pygame.Color(255, 255, 255, 255))

        return Text(chars, "", pygame.Vector2(0, 0), 1)

    @classmethod
    def fromImageSheet(cls, image: str | pygame.Surface, spriteSize: pygame.Vector2, spacings: pygame.Vector2 = pygame.Vector2(0, 0), *charNames):
        spr = pygame.image.load(image)
        splitRect = pygame.FRect(spacings, spriteSize)

        chars = {}
        for char in charNames:
            if spr.get_rect().contains(splitRect):
                splitRect.x = spacings.x
                splitRect.y += spriteSize.y + spacings.y

            chars[char] = spr.subsurface(splitRect)
            splitRect.x += spriteSize.x + spacings.x

        return Text(chars, "", pygame.Vector2(), 1)
