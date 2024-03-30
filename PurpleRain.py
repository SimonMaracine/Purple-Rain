#background_color (165, 165, 165)
#drop_color (128, 1, 128)

from random import uniform
import pygame
pygame.init()
screen = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Purple Rain")
clock = pygame.time.Clock()

run = True
screen_width = 1100
screen_height = 700
background_color = (165, 165, 165)
description_color = (100, 1, 100)
start = False
text = pygame.font.SysFont("calibri", 14)
instruction = text.render("Press space to start/stop purple rain", 1, (118, 5, 118))
description1 = text.render("Coded with love by me. Because I like purple.", 1, description_color)
description2 = text.render("Inspired by The Coding Train.", 1, description_color)
render_description = False

class Drop(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vel = 0
        self.gravity = 0
        self.width = width
        self.height = height
        self.color = (128, 1, 128)

    def show(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.vel += self.gravity
        self.y += self.vel
        if start:
            if self.y > screen_height:
                self.y = uniform(-300, -0)
                self.x = uniform(0, screen_width)
                self.vel = uniform(15, 18)

def draw():
    screen.fill(background_color)
    if not render_description:
        screen.blit(instruction, (screen_width - 220, screen_height - 20))
    else:
        screen.blit(description1, (screen_width - 267, screen_height - 40))
        screen.blit(description2, (screen_width - 190, screen_height - 20))
    for drop in drops:
        drop.update()
        drop.show()
    pygame.display.update()

drops = []
for i in range(60):
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 3.5, 16.5))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 3.2, 15.5))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 3, 15))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 2.8, 14.5))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 2.5, 13))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 2.2, 12))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 1.9, 11))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 1.7, 9))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 1.3, 6))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 1, 4.9))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 0.8, 3.9))
    drops.append(Drop(uniform(0, screen_width), uniform(-4000, -1000), 0.5, 3.7))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if start == False:
                start = True
                for drop in drops:
                    drop.vel = uniform(14.5, 17.5)
                    drop.x = uniform(0, screen_width)
                    drop.y = uniform(-3000, -1000)
                    drop.gravity = 0.01
            else:
                start = False
                render_description = True
# If you read this, it means that you truly appreciate my work.
# Thank you! :)
    draw()
    clock.tick(70)
pygame.quit()
