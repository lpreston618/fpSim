import pygame

WIDTH, HEIGHT = 1000, 500

def main():
    pygame.init()

    screen = pygame.display.set_mode(size = flags=(pygame.SCALED | pygame.RESIZABLE))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

main()