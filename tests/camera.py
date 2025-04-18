from engineV3 import Engine, Camera, Sprite, draw
import pygame

engine = Engine()
# engine.MainCamera.off()


# cam1 = Camera(0, 0, engine.Size.x / 2, engine.Size.y / 2)
# cam2 = Camera(engine.Size.x / 2, 0, engine.Size.x / 2, engine.Size.y / 2)
# cam3 = Camera(0, engine.Size.y / 2, engine.Size.x / 2, engine.Size.y / 2)
# cam4 = Camera(*(engine.Size / 2), *(engine.Size / 2))


surf = pygame.Surface((100, 100))
surf.fill((255, 255, 255))
spr = Sprite(surf)

def main():
    spr.angle += 1
    if engine.Input["d"].Held:
        engine.MainCamera.WorldPos.x -= 3

    if engine.Input["a"].Held:
        engine.MainCamera.WorldPos.x += 3

engine.mainState = main
engine.run()