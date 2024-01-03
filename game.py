import pygame
from random import choice
import os, sys
from dots import Bars, Goal
from population import Population



# window constants
WIN_WIDTH = 800
WIN_HEIGHT = 600


BG_IMG = pygame.image.load(os.path.join("assets", "background.png"))


def draw_window(window: pygame.Surface, p:Population, bars: list[Bars], goal: Goal) -> None:
    window.blit(BG_IMG, (0, 0))
    goal.draw(window)

    for bar in bars:
        bar.draw(window)
    p.draw(window)
    
    pygame.display.flip()

# def draw_window(window: pygame.Surface, dots: list[Dots], inactive: list[Dots], bars: list[Bars], goal: Goal) -> None:
#     window.blit(BG_IMG, (0, 0))
#     goal.draw(window)

#     for bar in bars:
#         bar.draw(window)
        
#     for dot in dots:
#         dot.draw(window)

#     for dot in inactive:
#         dot.draw(window)
#     pygame.display.flip()




# bar presets
set1 = [Bars(200, 350), Bars(-200, 150)]
set2 = [Bars(200, 150), Bars(-200, 350)]

def main():
    # dots = [Dots() for _ in range(1)]
    # inactive = []
    p = Population(100, [6, 4, 3])
    bars = choice([set1, set2])
    goal = Goal()

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    game_active = True
    flag = True

    while game_active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                p.get_fitness()
                pygame.quit()
                sys.exit()
                break
        
        p.update(goal, bars)
        draw_window(window, p, bars, goal)
        if p.fittest>0: print(f'-------------{p.fittest}-------------')
    


    # print(dots[0].img_width, dots[0].img_height)

    # while game_active:
    #     clock.tick(60)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             game_active = False
    #             pygame.quit()
    #             break
        
    #     dead = []

    #     for bar in bars:
    #         for dot in dots:
    #             if dot.alive:
    #                 key = pygame.key.get_pressed()
    #                 dot.move(key)
    #                 print("bar:", dot.distance_to(bar))
    #                 print("goal:", dot.distance_to(goal))

                    
    #                 if bar.collides(dot):
    #                     dot.kill()
    #                     dead.append(dot)

    #     for dot in dots:             
    #         if goal.collides(dot):
    #             dead.append(dot)
        
    #     for dot in dead:
    #         dots.remove(dot)
    #         inactive.append(dot)

    #     draw_window(window, dots, inactive, bars, goal)


main()