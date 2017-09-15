import pygame

pygame.init()
screen = pygame.display.set_mode((200, 300), pygame.RESIZABLE)

screen.fill((255,155,55))
pygame.display.flip()

class Application(object):
    def __init__(self):
        self.running = False

    def handleEvent(self, ev):
        if ev.type == pygame.QUIT:
            self.handleQuit(ev)    
        if ev.type == pygame.KEYUP:
            self.handleKeyUpEvent(ev)

    def handleQuit(self, ev):
        self.running = False

    def handleKeyUpEvent(self, ev):
        if ev.key in (ord('q'), pygame.K_ESCAPE):
            self.running = False

    def run(self):
        self.running = True
        while self.running:
            ev = pygame.event.wait()
            self.handleEvent(ev)



while True:

    ev = pygame.event.wait()

    if ev.type == pygame.KEYDOWN:
        print ev.key == ord('f')
        if ev.key == pygame.K_ESCAPE or :
            break



    if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
        # Display in Fullscreen mode
        pygame.display.quit()
        pygame.display.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3:
        # Display in Resizable mode
        pygame.display.quit()
        pygame.display.init()
        screen = pygame.display.set_mode((200, 300), pygame.RESIZABLE)

    print ev

    screen.fill((255,155,55))
    pygame.display.flip()