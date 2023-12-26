import pygame
from random import choice
import os
import math


# window constants
WIN_WIDTH = 800
WIN_HEIGHT = 600


# images
DOT_IMG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dot.png")), (10, 10))
BAR_IMG = pygame.image.load(os.path.join("assets", "bar.png"))
GOAL_IMG = pygame.image.load(os.path.join("assets", "goal.png"))
BG_IMG = pygame.image.load(os.path.join("assets", "background.png"))


class Dots:
    def __init__(self) -> None:
        self.img = DOT_IMG
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

        self.x = WIN_WIDTH//2 - self.img_width
        self.y = WIN_HEIGHT - self.img_height - 10
        self.speed = 2
        self.alive = True
        self.winner = False

    
    def move_right(self):
        print("moving right", self.x, self.y)
        self.x += self.speed
    
    def move_left(self):
        print("moving left", self.x, self.y)
        self.x -= self.speed

    def move_up(self):
        print("moving up", self.x, self.y)
        self.y -= self.speed

    def move_down(self):
        print("moving down", self.x, self.y)
        self.y += self.speed


    def move(self, key: pygame.key.ScancodeWrapper) -> None:

        if key[pygame.K_RIGHT]: self.move_right()
        if key[pygame.K_LEFT]: self.move_left()
        if key[pygame.K_UP]: self.move_up()
        if key[pygame.K_DOWN]: self.move_down()
        
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.img, (self.x, self.y))


    def get_mask(self) -> pygame.Mask:
        return pygame.mask.from_surface(self.img)
    
    def kill(self) -> None:
        self.alive = False
    
    def distance_to(self, obj) -> int:
        x1 = self.x
        if obj.x <= x1 <= obj.x + obj.img_width:
            x2 = x1
        elif x1 < obj.x:
            x2 = obj.x
        else: x2 = obj.x + obj.img_width

        y1 = self.y
        if obj.y <= y1 <= obj.y + obj.img_height:
            y2 = y1
        elif y1 < obj.y:
            y2 = obj.y
        else: y2 = obj.y + obj.img_height
        
        return math.hypot(x2-x1, y2-y1)




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
        offset = (self.x - dot.x, self.y - dot.y)

        if dot_body.overlap(bar_body, offset):
            print("collides")
            return True
        
        if (dot.x == 0 or dot.x + dot.img_width == WIN_WIDTH
            or dot.y == 0 or dot.y + dot.img_height == WIN_HEIGHT):
            print("out of bounds")
            return True


        return False


class Goal:
    def __init__(self) -> None:
        self.x = WIN_WIDTH//2 - 80
        self.y = 50

        self.img = GOAL_IMG
        self.img_width = self.img.get_width()
        self.img_height = self.img.get_height()

    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.img, (self.x, self.y))

    
    def get_mask(self) -> pygame.Mask:
        return pygame.mask.from_surface(self.img)


    def collides(self, dot: Dots) -> bool:
        dot_body = dot.get_mask()
        goal_body = self.get_mask()
        offset = (self.x - dot.x, self.y - dot.y)

        if dot_body.overlap(goal_body, offset):
            print("wins")
            dot.winner = True
            return True
        
        return False


def draw_window(window: pygame.Surface, dots: list[Dots], inactive: list[Dots], bars: list[Bars], goal: Goal) -> None:
    window.blit(BG_IMG, (0, 0))
    goal.draw(window)

    for bar in bars:
        bar.draw(window)
        
    for dot in dots:
        dot.draw(window)

    for dot in inactive:
        dot.draw(window)
    pygame.display.flip()




# bar presets
set1 = [Bars(200, 350), Bars(-200, 150)]
set2 = [Bars(200, 150), Bars(-200, 350)]

def main():
    dots = [Dots() for _ in range(1)]
    inactive = []
    bars = choice([set1, set2])
    goal = Goal()

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    game_active = True

    print(dots[0].img_width, dots[0].img_height)

    while game_active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                pygame.quit()
                break
        
        dead = []

        for bar in bars:
            for dot in dots:
                if dot.alive:
                    key = pygame.key.get_pressed()
                    dot.move(key)
                    print("bar:", dot.distance_to(bar))
                    print("goal:", dot.distance_to(goal))

                    
                    if bar.collides(dot):
                        dot.kill()
                        dead.append(dot)

        for dot in dots:             
            if goal.collides(dot):
                dead.append(dot)
        
        for dot in dead:
            dots.remove(dot)
            inactive.append(dot)

        draw_window(window, dots, inactive, bars, goal)


main()