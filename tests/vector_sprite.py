from engineV3 import Engine, VectorSprite
import pygame  # Pygame-CE


engine = Engine()
s = pygame.Surface((100, 100))
s.fill(pygame.Color("red"))
spr = VectorSprite(s)
spr.pos = pygame.Vector2(100, 100)
spr.Velocity = pygame.Vector2(1, 1)

def main():
    spr.pos += spr.Velocity
    spr.RotateSpeed = 1
    spr.angle += spr.RotateSpeed
    spr.draw()

engine.mainState = main
engine.run()