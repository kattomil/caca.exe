import pygame
from pygame.locals import *
import time
import random 

from .load import *
from .music import *

class Menu:
    def print_menu(screen):
        screen.blit(Load.menu, [1180, 0])

    def click_menu(screen):
        screen.blit(Load.menu_opened, [880, 0])
        Chomp.print_counter(screen)

class Action(object):
    atemoney = 0
    thisblob = Load.blob

class Player_Positions(object):
    x = 20
    y = 450

class Money_Positions(object):
    x = 300
    y = 470

class Chomp:
    def print_counter(screen):
        font = pygame.font.Font(None, 100)
        counter = font.render("Points: " + str(Action.atemoney), True, 'Black')
        screen.blit(counter, [880, 20])

    def eat(screen):
        if (Money_Positions.x>=Player_Positions.x-100 and Money_Positions.x<=Player_Positions.x+250) and (Money_Positions.y>=Player_Positions.y and Money_Positions.y<=Player_Positions.y+215):
            Play.play_chomp()
            Money_Positions.y = 470
            while Money_Positions.x>=Player_Positions.x-100 and Money_Positions.x<=Player_Positions.x+150:
                Money_Positions.x = random.randint(20, 1000)
            up = random.randint(0, 1)
            if up==1:
                Money_Positions.y -= random.randint(100, 200)
            Action.atemoney += 1

class Movement:
    def jump(screen, background_image, print_the_menu):
        Play.play_jump()
        saveblob = Action.thisblob
        if saveblob == Load.blob:
            Action.thisblob = Load.BlobJumpSus
        else:
            Action.thisblob = Load.BlobJumpSus2
        for i in range(200):
            Player_Positions.y -= 1
            if i%50==0:
                screen.blit(background_image, [0, 0])
                screen.blit(Load.money, [Money_Positions.x, Money_Positions.y])
                Menu.print_menu(screen)
                screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
                if print_the_menu==1:
                    Menu.click_menu(screen)
                if print_the_menu==0:
                    Menu.print_menu(screen)
                pygame.display.flip()
                time.sleep(0.1)

        Chomp.eat(screen)

        if saveblob == Load.blob:
            Action.thisblob = Load.BlobJumpJos
        else:
            Action.thisblob = Load.BlobJumpJos2
            
        for i in range(200):
            Player_Positions.y += 1
            if i%50==0:
                screen.blit(background_image, [0, 0])
                screen.blit(Load.money, [Money_Positions.x, Money_Positions.y])
                Menu.print_menu(screen)
                screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
                if print_the_menu==1:
                    Menu.click_menu(screen)
                if print_the_menu==0:
                    Menu.print_menu(screen)
                pygame.display.flip()
                time.sleep(0.1)
        Action.thisblob = saveblob

    def left(screen):
        Play.play_movement()
        Player_Positions.x -= 50
        Action.thisblob = Load.BlobZdrobit
        screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
        pygame.display.flip()
        Action.thisblob = Load.blob2
        time.sleep(0.5)

    def right(screen):
        Play.play_movement()
        Player_Positions.x += 50
        Action.thisblob = Load.BlobZdrobit2
        screen.blit(Action.thisblob, (Player_Positions.x, Player_Positions.y))
        pygame.display.flip()
        Action.thisblob = Load.blob
        time.sleep(0.5)