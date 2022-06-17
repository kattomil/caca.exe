import pygame
from pygame.locals import *

from files.load import *
from files.actions import *
from files.music import *

pygame.init()

screen = pygame.display.set_mode((1280, 720))
background_image = pygame.image.load("assets/background.png").convert()

pygame.display.set_caption("caca.exe")
Play.play_forest()

running = True
clock = pygame.time.Clock()

print_the_menu = 0

while running:
    screen.blit(background_image, [0, 0])
    screen.blit(Load.money, [Money_Positions.x, Money_Positions.y])
    if print_the_menu==1:
        Menu.click_menu(screen)
    if print_the_menu==0:
        Menu.print_menu(screen)

    key = pygame.key.get_pressed()

    if (key[K_a] or key[K_LEFT]) and Player_Positions.x>20:
        Movement.left(screen)
    elif (key[K_d] or key[K_RIGHT]) and Player_Positions.x<1000:
        Movement.right(screen)
    elif (key[K_SPACE] or key[K_w]) or key[K_UP]:
        Movement.jump(screen, background_image, print_the_menu)
    else:
        screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
        pygame.display.flip()

    Chomp.eat(screen)
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        click = pygame.mouse.get_pressed()
        click_pos = pygame.mouse.get_pos()
        if click == (1, 0, 0) and (click_pos[0]>=1180 and click_pos[0]<=1280) and (click_pos[1]>=0 and click_pos[1]<=100):
            if print_the_menu == 1:
                print_the_menu = 0
            else:
                print_the_menu = 1

    clock.tick(60)

pygame.quit()