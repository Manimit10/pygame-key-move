import pygame

pygame.init()

# create display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('keyboard')

# set game value
VELOCITY = 10

#load in images
dragon_image = pygame.image.load('dragon_right.png')
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = WINDOW_WIDTH//2
dragon_rect.bottom = WINDOW_HEIGHT


# main game loop
running = True
while running:
    for event in pygame.event.get():
        # if you want to see all events in terminal
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        # chack for discrete movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
                # print('left')
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
                # print('right')
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY

    # reset the screen
    display_surface.fill((0, 0, 0))
    # Blit
    display_surface.blit(dragon_image, dragon_rect)
    # Update the display
    pygame.display.update()

# End the game
pygame.quit()
