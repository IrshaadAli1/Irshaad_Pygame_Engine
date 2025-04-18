from engineV3 import Engine
import pygame  # Pygame-CE

engine = Engine()
rectColors = [(pygame.FRect(10, 10, 100, 100), pygame.Color("red")), (pygame.FRect(50, 50, 50, 50), pygame.Color('blue'))]

def main():
    for rc in rectColors:
        pygame.draw.rect(engine.Screen, rc[1], rc[0])

engine.mainState = main
engine.run()