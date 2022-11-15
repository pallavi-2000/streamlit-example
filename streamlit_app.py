pip install pygame
#2D Graphics library

import pygame
import math
pygame.init()
#initialize all imported pygame modules is a convenient way to get everything started

#first thing setting up a pygame window setting up width & height in pixels
width,height =800, 800

#This function will create a display Surface
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Planet Simulation")

#we will now make a loop

def main():
  run=True

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run=False
  pygame.quit()

main()
