import pygame as pg
from settings import *
from planet import Planet

class PlanetManager:
    def __init__(self, screen) -> None:
        self.planets = pg.sprite.Group()
        self.add_planet()
        self.screen = screen
    
    def add_planet(self):
        self.planets.add(Planet((100, 100)))
        
    def render(self):
        self.planets.draw(self.screen)
    
    def update(self):
        self.planets.update()