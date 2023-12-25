import pygame
import random
import os

WIN_WIDTH = 800
WIN_HEIGHT = 600

DOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dot.png")), 0.01)
BAR_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bar.png")))

class Dots:
    def __init__(self) -> None:
        self.x = WIN_WIDTH//2
        self.y = WIN_HEIGHT - 10

        self.img = DOT_IMG
    
    
    def move(self, key: pygame.key.ScancodeWrapper) -> None:
        if key[pygame.K_RIGHT]:
            self.x +=1
        if key[pygame.K_LEFT]:
            self.x -= 1
        if key[pygame.K_UP]:
            self.y += 1
        if key[pygame.K_DOWN]:
            self.y -= 1
        

    def get_mask(self) -> pygame.Mask:
        return pygame.mask.from_surface(self.img)


def main():
    dot = Dots()
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()