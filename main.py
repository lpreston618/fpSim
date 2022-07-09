import pygame
import assets

WIDTH, HEIGHT = 1000, 500

def main():
    pygame.init()
    #switch_list = []

    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #if event.type == pygame.mouse.get_pressed():
                
    
    pygame.quit()

main()


class SWITCH:
    def __init__(self,x,y):
        self.loc = (x,y)
        self.dim = (100,100)
        self.pic_on = pygame.image.load('assets/switch-on.jpg')
        self.pic_off = pygame.image.load('assets/switch-off.jpg')
        self.current_pic = self.pic_off
        self.state = False
        self.rect = pygame.rect(self.loc,self.dim)
    
    def changeState(self):
        if self.state == False:
            self.state = True
            self.current_pic = self.pic_on

        if self.state == True:
            self.state = False
            self.current_pic = self.pic_off

    def initializeOnScreen(self):
        screen.blit(self.current_pic)
