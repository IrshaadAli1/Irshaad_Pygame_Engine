from engineV3 import Engine, Sprite
import pygame  # Pygame-CE


engine = Engine()
s = pygame.Surface((100, 100))
s.fill(pygame.Color("red"))
spr = Sprite(s)
spr.pos = pygame.Vector2(100, 100)

def main():
    spr.pos += pygame.Vector2(1, 1)
    spr.angle += 1
    spr.draw()

engine.mainState = main
engine.run()