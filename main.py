import pygame as pg
from settings import *
from shuttle_manager import ShuttleManager
from camera import Camera
from planet_manager import PlanetManager

class Game():
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.is_running = True
        self.setup()
    
    def setup(self):
        self.shuttle_manager = ShuttleManager(self.screen)
        self.camera = Camera(self.shuttle_manager.shuttles[0].pos)
        self.shuttle_manager.camera = self.camera
        self.planet_manager = PlanetManager(self.screen)
    
    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
    
    def render(self):
        self.screen.fill('black')
        self.planet_manager.render()
        self.shuttle_manager.render()

    def update(self):
        self.shuttle_manager.update()
        self.planet_manager.update()
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def run(self):
        while self.is_running:
            self.event_loop()
            self.update()
            self.render()
        pg.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

 