import pygame
from random import randint
import os

WIN_WIDTH = 800
WIN_HEIGHT = 600

DOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dot.png")), (15, 15))
BAR_IMG = pygame.image.load(os.path.join("assets", "bar.png"))
BG_IMG = pygame.image.load(os.path.join("assets", "background.png"))

class Dots:
    def __init__(self) -> None:
        self.img = DOT_IMG
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

        self.x = WIN_WIDTH//2 - self.img_width
        self.y = WIN_HEIGHT - self.img_height - 10
        self.speed = 1
        self.alive = True

    
    
    def move(self, key: pygame.key.ScancodeWrapper) -> None:

        if key[pygame.K_RIGHT]:
            print("moving right", self.x, self.y)
            self.x += self.speed
        if key[pygame.K_LEFT]:
            print("moving left", self.x, self.y)
            self.x -= self.speed
        if key[pygame.K_UP]:
            print("moving up", self.x, self.y)
            self.y -= self.speed
        if key[pygame.K_DOWN]:
            print("moving down", self.x, self.y)
            self.y += self.speed
        
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.img, (self.x, self.y))


    def get_mask(self) -> pygame.Mask:
        return pygame.mask.from_surface(self.img)
    
    def kill(self) -> None:
        self.alive = False


class Bars:
    def __init__(self, x=400, y=500) -> None:
        self.x = x
        self.y = y

        self.img = BAR_IMG
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.img, (self.x, self.y))

    
    def get_mask(self) -> pygame.Mask:
        return pygame.mask.from_surface(self.img)


    def collides(self, dot: Dots) -> bool:
        dot_body = dot.get_mask()
        bar_body = self.get_mask()
        overlap = (self.x - dot.x, self.y - dot.y)

        if dot_body.overlap(bar_body, overlap):
            print("collides")
            return True
        
        return False


def draw_window(window: pygame.Surface, dots: list[Dots], bars: list[Bars]) -> None:
    window.blit(BG_IMG, (0, 0))
    for bar in bars:
        bar.draw(window)
        
    for dot in dots:
        dot.draw(window)
    pygame.display.update()



def main():
    dots = [Dots() for _ in range(1)]
    bars = [Bars(randint(-750, 750), randint(150, 400)) for _ in range(2)]
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    game_active = True

    while game_active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                pygame.quit()
                break
        for bar in bars:
            for dot in dots:
                if dot.alive:
                    key = pygame.key.get_pressed()
                    dot.move(key)
                    
                    if bar.collides(dot):
                        dot.kill()
                
        draw_window(window, dots, bars)


main()