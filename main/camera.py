from .engine import Base
import pygame

class Camera(Base):
    def __init__(self, x, y, w, h):
        super().__init__()

        self.WorldPos = pygame.Vector2()
        self.Rect = pygame.Rect(x, y, w, h)
        self.Zoom = 1
        self.Track = None

        self.on()

    def _ifTrack(self):
        if self.Track is not None:
            curX = self.WorldPos.x
            curY = self.WorldPos.y

            tarX = self.Track.pos.x + self.Track.size.x / 2
            tarY = self.Track.pos.y + self.Track.size.y / 2

            self.WorldPos = pygame.Vector2(
                (curX * 0.95) + (tarX * 0.05),
                (curY * 0.95) + (tarY * 0.05)
            )

    def render(self, *sprites):
        objects = sprites
        self.Engine.Screen.set_clip(self.Rect)

        self._ifTrack()

        def renderObj(spr):
            size = spr.size.copy()
            pos = spr.pos.copy()

            spr.pos = pygame.Vector2((spr.pos.x * self.Zoom) + self.Offset.x, (spr.pos.y * self.Zoom) + self.Offset.y)
            spr.size = pygame.Vector2(spr.size.x * self.Zoom, spr.size.y * self.Zoom)
            spr.draw()
            spr.pos = pos.copy()
            spr.size = size.copy()

        if len(objects) > 0 and isinstance(objects[0], list | tuple):

            for obj in objects:
                for spr in obj:
                    renderObj(spr)
        else:
            for spr in objects:
                renderObj(spr)

        self.Engine.Screen.set_clip(None)

    def blitSurface(self, surface: pygame.Surface, dest: pygame.Rect | pygame.Vector2, area: pygame.Rect = None, angle: int = 0, flipX: bool = False, flipY: bool = False):
        if area is not None: image = surface.copy().convert_alpha().subsurface(area)
        else: image = surface.copy().convert_alpha()
        self.Engine.Screen.set_clip(self.Rect)

        self._ifTrack()

        image = pygame.transform.flip(pygame.transform.rotate(image, -angle),
                                      flipX, flipY)
        rect = image.get_frect(center=((dest[0] * self.Zoom) + self.Offset.x, (dest[1] * self.Zoom) + self.Offset.y))
        self.Engine.Screen.blit(image, rect)
        self.Engine.Screen.set_clip(None)

    @property
    def Offset(self):
        return pygame.Vector2(
            self.Rect.centerx - (self.WorldPos.x * self.Zoom),
            self.Rect.centery - (self.WorldPos.y * self.Zoom)
        )

    def on(self):
        if self.Engine.Cameras.__contains__(self): return
        self.Engine.Cameras.append(self)

    def off(self):
        if not self.Engine.Cameras.__contains__(self): return
        self.Engine.Cameras.remove(self)