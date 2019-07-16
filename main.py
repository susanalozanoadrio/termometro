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
        self.value(value)
        
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)
        
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
            
    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass
            
    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
            
    def size(self, val = None):
        if val == None:
                return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
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
        self.entrada = NumberInput('21')
        self.entrada.pos((150, 58))
        self.entrada.size((133, 30))
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            #pintamos el termometro en su posicion        
            self.__screen.blit(self.termometro.custome, (30, 34))
            #pintamos el cuadro de texto
            text = self.entrada.render() #Obtenemos el rectangulo blanco y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) #creamos el rectangulo blanco en su posicion y tamaño posicion 
            self.__screen.blit(text[1], self.entrada.pos()) #pintamos la foto del texto
            pygame.display.flip()
                    
                    
if __name__ =='__main__':
    pygame.init()
    app = mainApp()
    app.start()
