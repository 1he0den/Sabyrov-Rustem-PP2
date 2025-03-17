import pygame # type: ignore

pygame.init()
screen = pygame.display.set_mode((1000, 700))
done = False

x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - 25 >= 23: y -= 25
        if pressed[pygame.K_DOWN] and y + 25 <= 690: y += 25
        if pressed[pygame.K_LEFT] and x - 25 >= 23: x -= 25
        if pressed[pygame.K_RIGHT] and x + 25 <= 990: x += 25
        
        screen.fill((255, 255, 255))
        color = (255, 0, 0)
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(55)