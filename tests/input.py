from engineV3 import Engine, Sprite
import pygame  # Pygame-CE


engine = Engine()
s = pygame.Surface((100, 100))
s.fill(pygame.Color("red"))
spr = Sprite(s)
spr.pos = pygame.Vector2(100, 100)
Input = engine.Input


def main():
    if Input["d", "right"].Held:
        spr.pos.x += 3
    if Input["left", "a"].Held:
        spr.pos.x -= 3
    if Input["up", "w"].Held:
        spr.pos.y -= 3
    if Input["down", "s"].Held:
        spr.pos.y += 3

    if Input[all, "q", "e"].Held:
        spr.angle += 1
    spr.draw()

engine.mainState = main
engine.run()