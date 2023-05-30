from shuttle import Shuttle
import pygame as pg
class ShuttleManager:
    def __init__(self, screen) -> None:
        self.shuttles = []
        self.shuttles.append(Shuttle())
        self.screen = screen
        self.camera = None

    def update(self):
        for shuttle in self.shuttles:
            shuttle.update()
            
    def render(self):
        for shuttle in self.shuttles:
            shuttle_pos_x = shuttle.pos.x
            shuttle_pos_y = shuttle.pos.y
            shuttle_pos = shuttle_pos_x, shuttle_pos_y
            shuttle_pos = self.camera.apply(shuttle_pos)
            shuttle_vec = pg.Vector2(shuttle_pos)
            print(shuttle_vec, shuttle.pos)
            # pg.draw.rect(self.screen, (255, 255, 255), (shuttle_vec.x, shuttle_vec.y, 20, 20))
            # pg.draw.rect(self.screen, (255, 255, 255), (shuttle.pos.x, shuttle.pos.y, 20, 20))
            pg.draw.polygon(self.screen, (255, 255, 255), shuttle.triangle_points)
            
    
