import pygame as pg
from settings import *
class Camera:
    def __init__(self, target) -> None:
        self.target: pg.Vector2 = target
        self.offset = pg.Vector2(WIDTH//2, HEIGHT//2)
        
    def apply(self, entity: pg.Vector2):
        return entity - self.target + self.offset