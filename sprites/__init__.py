from ..main.engine import Base
from ..utils import loadImage
import pygame

class Sprite(Base):
    def __init__(self, img: pygame.Surface | str):
        super().__init__()
        self.image = loadImage(img).convert_alpha() if isinstance(img, str) else img.convert_alpha()
        self.rect = self.image.get_frect()
        self.mask = pygame.mask.from_surface(self.image)

        self.hitbox: pygame.rect.FRect = None

        self.pos = pygame.math.Vector2(self.rect.center)
        self.size = pygame.math.Vector2(self.rect.size)

        self.angle = 0
        self.flipX = False
        self.flipY = False

        self.color = None
        self.blend = 0

        self.show()

    def render(self):
        image = self.image.copy()

        if self.color is not None:
            image.fill(self.color, special_flags=self.blend)

        image = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(image, self.size), -self.angle), self.flipX, self.flipY)
        self.rect = image.get_frect(center=self.pos)
        if self.hitbox:
            self.hitbox.center = self.rect.center
        self.mask = pygame.mask.from_surface(image)
        return image

    def draw(self):
        self.Engine.Screen.blit(self.render(), self.rect)

    def collideRect(self, rect):
        return self.rect.colliderect(rect)

    def collideRects(self, *rects):
        return self.rect.collidelist(rects)

    def collideAllRects(self, *rects):
        return self.rect.collidelistall(rects)

    def collidePoint(self, point):
        return self.rect.collidepoint(point)

    def collideMask(self, other):
        return pygame.sprite.collide_mask(self, other)

    def collideHitbox(self, rect):
        if self.hitbox is None: return False
        return self.hitbox.colliderect(rect)

    def show(self):
        if self.Engine.Sprites.__contains__(self): return
        self.Engine.Sprites.append(self)

    def hide(self):
        if not self.Engine.Sprites.__contains__(self): return
        self.Engine.Sprites.remove(self)


class VectorSprite(Sprite):
    def __init__(self, img: pygame.Surface | str):
        super().__init__(img)
        self.Velocity = pygame.math.Vector2()
        self.Acceleration = pygame.math.Vector2()
        self.RotateSpeed = 0
