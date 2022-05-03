import pygame
from options import *

#Stores image reference variables for each character and more

#Pacman
pacRightOpen = pygame.transform.scale(pygame.image.load("Images/pacman_open.png"), (tile_size, tile_size))
pacLeftOpen = pygame.transform.rotate(pacRightOpen, 180)
pacUpOpen = pygame.transform.rotate(pacRightOpen, 90)
pacDownOpen = pygame.transform.rotate(pacRightOpen, 270)

pacRightClosed = pygame.transform.scale(pygame.image.load("Images/pacman_closed.png"), (tile_size, tile_size))
pacLeftClosed = pygame.transform.rotate(pacRightClosed, 180)
pacUpClosed = pygame.transform.rotate(pacRightClosed, 90)
pacDownClosed = pygame.transform.rotate(pacRightClosed, 270)

#Coins
coin = pygame.transform.scale(pygame.image.load("Images/pacman_closed.png"), (int(tile_size/2.35), int(tile_size/2.35)))

#Blinky
blinky_up = pygame.transform.scale(pygame.image.load("Images/blinky_up.png"), (tile_size, tile_size))
blinky_down = pygame.transform.scale(pygame.image.load("Images/blinky_down.png"), (tile_size, tile_size))
blinky_left = pygame.transform.scale(pygame.image.load("Images/blinky_left.png"), (tile_size, tile_size))
blinky_right = pygame.transform.flip(blinky_left, True, False)

#Pinky
pinky_up = pygame.transform.scale(pygame.image.load("Images/pinky_up.png"), (tile_size, tile_size))
pinky_down = pygame.transform.scale(pygame.image.load("Images/pinky_down.png"), (tile_size, tile_size))
pinky_left = pygame.transform.scale(pygame.image.load("Images/pinky_left.png"), (tile_size, tile_size))
pinky_right = pygame.transform.flip(pinky_left, True, False)

#Inky
inky_up = pygame.transform.scale(pygame.image.load("Images/inky_up.png"), (tile_size, tile_size))
inky_down = pygame.transform.scale(pygame.image.load("Images/inky_down.png"), (tile_size, tile_size))
inky_left = pygame.transform.scale(pygame.image.load("Images/inky_left.png"), (tile_size, tile_size))
inky_right = pygame.transform.flip(inky_left, True, False)

#Clyde
clyde_up = pygame.transform.scale(pygame.image.load("Images/clyde_up.png"), (tile_size, tile_size))
clyde_down = pygame.transform.scale(pygame.image.load("Images/clyde_down.png"), (tile_size, tile_size))
clyde_left = pygame.transform.scale(pygame.image.load("Images/clyde_left.png"), (tile_size, tile_size))
clyde_right = pygame.transform.flip(clyde_left, True, False)