import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("img/termometro1.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        elif toUnidad == 'F':
            resultado = grados * 9/5 + 32
        else:
            resultado = grados
            
        return "{:9.2f}".format(resultado)

class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = 'C'):
        self.__customes = []
        self.__customes.append(pygame.image.load("img/c.png"))
        self.__customes.append(pygame.image.load("img/f.png"))
        
        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == 'C':
            return self.__customes[0]
        else:
            return self.__customes[1]
        
    def change(self):
        if self.__tipoUnidad == 'C':
            self.__tipoUnidad = 'F'
        else:
            self.__tipoUnidad ='C'
            
    def unidad(self):
        return self.__tipoUnidad
        
    
class NumberInput():
    __value = 0
    __strValue = ''
    __position = [0, 0]
    __size = [0, 0]
    __pointCount = 0
    
    def __init__(self, value =0):
        self.__font = pygame.font.SysFont('Arial', 24)
        self.value(value)
        
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == '.' and self.__pointCount == 0):
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointCount += 1
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == '.':
                    self.__pointCount -= 1
                self.__strValue = self.__strValue[0:-1]
                self.value(self.__strValue)
        
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
                self.__value = float(val)
                self.__strValue = val
                if '.' in self__strValue:
                    self.pointCount = 1
                else:
                    self.__pointCount = 0
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
        self.__screen = pygame.display.set_mode((380, 415))
        pygame.display.set_caption('Termómetro')
        
        
        self.termometro = Termometro()
        self.entrada = NumberInput('')
        self.entrada.pos((180, 58))
        self.entrada.size((133, 30))
        self.selector = Selector()
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    
                    self.entrada.value(temperatura)
                
            #pintamos el fondo de pantalla
            self.__screen.fill((142, 204, 80))
            #pintamos el termometro en su posicion        
            self.__screen.blit(self.termometro.custome, (30, 34))
            #pintamos el cuadro de texto
            text = self.entrada.render() #Obtenemos el rectangulo blanco y lo asignamos a text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0]) #creamos el rectangulo blanco en su posicion y tamaño posicion 
            self.__screen.blit(text[1], self.entrada.pos()) #pintamos la foto del texto
            self.__screen.blit(self.selector.custome(), (150, 130)) #pintamos la foto del selector
            pygame.display.flip()
                    
                    
if __name__ =='__main__':
    pygame.init()
    app = mainApp()
    app.start()
