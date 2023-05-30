import pygame as pg
from settings import *
from pygame.locals import *

class Shuttle:
    def __init__(self) -> None:
        self.pos = pg.Vector2(WIDTH//2, HEIGHT//2)
        self.vel = pg.Vector2(0, 0)
        self.acc = pg.Vector2(0, 0)
        self.speed = 0.03
        self.gravity = 0.0
        self.friction = 0.001
        self.rotation = 0
        self.rotation_speed = 1
        self.triangle_points = []

    def handle_input(self): 
        keys = pg.key.get_pressed()
        if keys[K_w]:
            self.acc = pg.Vector2(0, -self.speed).rotate(-self.rotation)
        elif keys[K_s]:
            self.acc = pg.Vector2(0, self.speed).rotate(-self.rotation)
        else: 
            self.acc.y = 0

        if keys[K_a]:
            self.rotation += self.rotation_speed
        elif keys[K_d]:
            self.rotation -= self.rotation_speed
        else:
            self.acc.x = 0
            
    def get_points(self):
        self.triangle_points = [
            pg.Vector2(0, -10).rotate(-self.rotation),
            pg.Vector2(8, 10).rotate(-self.rotation),
            pg.Vector2(-8, 10).rotate(-self.rotation)
        ]
        self.triangle_points = [p + self.pos for p in self.triangle_points]
        

    def update(self):
        self.handle_input()
        self.get_points()
        # Apply low gravity
        self.acc.y += self.gravity

        # Apply acceleration
        self.vel += self.acc

        # Apply friction
        self.vel.x *= 1 - self.friction
        self.vel.y *= 1 - self.friction

        # Limit maximum velocity
        self.vel.x = max(-0.5, min(0.5, self.vel.x))
        self.vel.y = max(-0.5, min(0.5, self.vel.y))

        # Update position
        self.pos += self.vel

        # Keep the player inside the screen boundaries
        # self.pos.x = max(0, min(width - 20, self.pos.x))
        # self.pos.y = max(0, min(height - 20, self.pos.y))
