import pygame

class Runtime:
    def __init__(self, fps: int = 60):
        self._Clock = pygame.time.Clock()
        self.FPS = fps
        self.getFPS = self._Clock.get_fps
        self.getTime = self._Clock.get_time
        self.getRawTime = self._Clock.get_rawtime

    def tick(self):
        self._Clock.tick(self.FPS)