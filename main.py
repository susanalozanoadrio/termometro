import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("img/termometro1.png")

class NumberInput():
    __value = 0
    __strValue = '0'
    __position = [0, 0]
    __size = [0, 0]
    
    def __init__(self, value =0):
        self.__font = pygame.font.SysFont('Arial', 24)
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rec.size = self.__size
        
    def value(self, val = None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val)
                self.__strValue = val
            except:
                pass
            
    def posX(self, val = None):
         if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass
            
     def posY(self, val = None):
         if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def pos(self, val = None):
          if val == None:
            return self.__position
        else:
            try:
                self.__position= [int(val[0]), int(val[1])]
            except:
                pass
    
          
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((310, 415))
        pygame.display.set_caption('Termómetro')
        self.__screen.fill((142, 204, 80))
        
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.width()
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                    
            self.__screen.blit(self.termometro.custome, (50, 34))        
            pygame.display.flip()
                    
                    
if __name__ =='__main__':
    pygame.init()
    app = mainApp()
    app.start()
