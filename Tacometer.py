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
        self.tacometer_measure = 0
        self.deg = 0
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
        self.ninety_deg = self.converter.deg_to_rad(90)
    
    def selectType(self, type):
        self.type = type
        
    def createMeterWindow(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Medidor")
        
    def set_tacometer_measure(self, tm):
        self.tacometer_measure = tm
    
    def initLoop(self):
        #self.background = pygame.Surface(self.size)
        #self.background.fill((255,0,255))
        self.clock = pygame.time.Clock()
        
        self.map_tacometer_measure_to_degree()
        
        #clock = pygame.time.Clock()
        while self.going:
            
            # lectura del teclado para cerrar la ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.going = False
            self.screen.fill(self.BACKG_COLOR)
            
            # el angulo de rotacion que va a dar la aguja respecto de cero en el eje x
            # este angulo debe de estar en radianes -> ejemplo: pi / 2
            angle = self.converter.deg_to_rad(self.map_tacometer_degree())
            
            self.draw_arc_semicircle()
            self.draw_center()
            self.draw_pointer(angle)
            self.deg+=1
            # mostrando la imagen o actualizando
            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.display.quit()
        
    def draw_arc_semicircle(self):
        #print("oh shit here we go again")
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
        
    def draw_pointer(self, angle):
        
        
        measure_x, measure_y = self.calculate_peak(angle)
        
        peak = (measure_x, measure_y)
        
        # bases respecto el angulo del pico del pointer
        base_i_angle = angle + self.ninety_deg
        base_d_angle = angle - self.ninety_deg
        
        #print("base i: {}, base d: {}".format(base_i_angle, base_d_angle))
        
        # i, d = punto central
        base_i_x, base_i_y = self.calculate_base(base_i_angle)
        base_d_x, base_d_y = self.calculate_base(base_d_angle)
        print("base i_x: {}, base i_y: {}".format(base_i_x, base_i_y))
        print("base d_x: {}, base d_y: {}".format(base_d_x, base_d_y))
        
        base_i = (base_i_x, base_i_y)
        base_d = (base_d_x, base_d_y)
        #base_i = (200, 190)
        #base_d = (200, 210)
        
        # usando un poligono de 3 nodos
        pygame.draw.polygon(self.screen, self.WHITE, [base_i, base_d, peak], 0)
        
    def calculate_peak(self, angle):
        # el angulo debe de llegar en radianes
        #xf = 400
        #xy = 200
        L = self.size[0] / 2
        x = math.cos(angle) * L
        y = math.sin(angle) * L
        xf = L + x
        yf = L - y
        return xf, yf
    
    def calculate_base(self, angle):
        center = self.size[0] / 2
        L = -10
        x = math.cos(angle) * L
        y = math.sin(angle) * L
        xf = center - x
        yf = center + y
        return xf, yf
    
    def map_tacometer_degree(self):
        # si es cero, este tiene que convertirse a 240 grados
        converted_deg = 240 - self.deg
        if self.deg >= 300:
            # el tope del tacometro, la parte final roja, esto es 360 - 60
            return -60
        return converted_deg
    
    def map_tacometer_measure_to_degree(self):
        # el tacometro va de cero a 60, los grados permisibles van de 0 - 300
        self.deg = self.tacometer_measure


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
    m.set_tacometer_measure(30)
    m.selectType(1)
    m.createMeterWindow()
    m.initLoop()
    
        
        