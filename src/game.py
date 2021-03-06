import pygame
from pygame.locals import *

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

class Text:
#Create a text object

    def set_font(self):
    #Set the font from its name and size
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
    #Render the text into an image
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def draw(self):
    #Draw the text image to the screen
        App.screen.blit(self.img, self.rect)


class App:
#creates the single-window app

    def do_shortcut(self, event):
    #Find the the key/mod combination in the dictionary and execute the cmd
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])
    

    def __init__(self):
    #initializes pygame and the app
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 640, 480)

    #creates resizable screen
        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.t = Text('Pygame App', pos=(20, 20))
        App.running = True


    def toggle_fullscreen(self):
    #Toggle between full screen and windowed screen
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((1280, 720), self.flags)

    def toggle_resizable(self):
    #Toggle between resizable and fixed-size window
        self.flags ^= RESIZABLE
        pygame.display.set_mode(self.rect.size, self.flags)

    def toggle_frame(self):
    #Toggle between frame and noframe window
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.rect.size, self.flags)

    def run(self):
    #Runs the main event loop

        self.shortcuts = {
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'print("ctrl+X")',
            (K_x, KMOD_LSHIFT): 'print("shift+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LALT + KMOD_LSHIFT): 'print("alt+shift+X")',
            (K_f, KMOD_LCTRL): 'self.toggle_fullscreen()',
            (K_r, KMOD_LCTRL): 'self.toggle_resizable()',
            (K_g, KMOD_LCTRL): 'self.toggle_frame()'
        }

        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                if event.type == KEYDOWN:
                    self.do_shortcut(event)
                
            App.screen.fill(WHITE)
            App.t.draw()
            pygame.display.update()

        pygame.quit()
if __name__ == '__main__':
    App().run()
