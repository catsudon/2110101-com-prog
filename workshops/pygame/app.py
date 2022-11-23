import pygame

width = 500
height = 300
FPS = 60

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Test_Pygame")

p_to_img = pygame.image.load("./milos.png").convert_alpha()
p_to_img = pygame.transform.scale(p_to_img, (500, 300))
p_to_rect = p_to_img.get_rect()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0,0,0))

    screen.blit(p_to_img, p_to_rect)
    pygame.display.flip()