import pygame
import assets

WIDTH, HEIGHT = 1000, 500

def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.mouse.get_pressed():
                
    
    pygame.quit()

main()


class SWITCH:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dim = ()
        self.pic_on = open('assets/switch-on.jpg')
        self.pic_off = open('assests/switch-off.jpg')
        self.state = False
        self.rect = pygame.rect((x,y),(w,h))