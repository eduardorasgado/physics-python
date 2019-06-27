# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import pygame

class Meter:
    def __init__(self, size, converter):
        print("Un medidor ha sido creado")
        self.type = 0
        self.size = size
        self.screen = None
        self.background = None
        self.going = True
        self.clock = None
        self.converter = converter
        self.BACKG_COLOR = (200,200,200)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        # izquierda, arriba, ancho, alto
        self.arc_rectangle = [0, 0,400,400]
        self.arc_thickness = 10
    
    def selectType(self, type):
        self.type = type
        
    def createMeterWindow(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Medidor")
    
    def initLoop(self):
        #self.background = pygame.Surface(self.size)
        #self.background.fill((255,0,255))
        self.clock = pygame.time.Clock()
        base_i = (200, 190)
        base_d = (200, 210)
        measure_angle_x = 0
        measure_angle_y = 200
        # i, d = punto central
        peak = (measure_angle_x, measure_angle_y)
        
        #clock = pygame.time.Clock()
        while self.going:
            # lectura del teclado para cerrar la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.going = False
            self.screen.fill(self.BACKG_COLOR)
            
            self.draw_arc_semicircle()
            self.draw_center()
            self.draw_pointer(base_i, base_d, peak)
            
            # mostrando la imagen o actualizando
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.display.quit()
        
    def draw_arc_semicircle(self):
        print("oh shit here we go again")
        start_rad = self.converter.deg_to_rad(240)
        stop_green_rad = self.converter.deg_to_rad(45)
        yellow_red_middle_rad = self.converter.inverted_deg_to_rad(10)
        max_rad = self.converter.inverted_deg_to_rad(60)
        
        # arco verde, desde 240 grados hasta los 45 grados
        pygame.draw.arc(self.screen, self.GREEN, self.arc_rectangle,
                        stop_green_rad, start_rad, self.arc_thickness)
        # arco amarillo
        pygame.draw.arc(self.screen, self.YELLOW , self.arc_rectangle, 
                        yellow_red_middle_rad, stop_green_rad, self.arc_thickness)
        ## arco rojo
        pygame.draw.arc(self.screen, self.RED , self.arc_rectangle, max_rad, 
                        yellow_red_middle_rad, self.arc_thickness)
        
    def draw_center(self):
        #pygame.draw.circle(self.screen, self.BLACK, [(100+(255-100)/2), 50+((255-50)/2)], 4, 0)
        pygame.draw.circle(self.screen, self.BLACK, [200,200], 8, 0)
        
    def draw_pointer(self, base_i, base_d, peak):
        # usando un poligono de 3 nodos
        pygame.draw.polygon(self.screen, self.WHITE, [base_i, base_d, peak], 0)


class ConversionOperations:
    def __init__(self):
        self.PI = math.pi
    
    def deg_to_rad(self, deg):
        return deg * (self.PI/180)
    
    def inverted_deg_to_rad(self, deg):
        return 0 - (deg * (self.PI/180))
                

    
if __name__=="__main__":
    size = (400, 400)
    converter = ConversionOperations()
    m = Meter(size, converter)
    m.selectType(1)
    m.createMeterWindow()
    m.initLoop()
    
        
        