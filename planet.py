import pygame as pg
import random 

class Planet(pg.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.pos = pg.Vector2(pos)
        self.size = random.randint(10, 50)
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size, self.size)
        self.image = pg.Surface([self.size, self.size])
        self.image.fill((255, 255, 200))
        
    
    def update(self):
        pass