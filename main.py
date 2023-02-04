"""
Main file of the polygon art simulation
"""

import pygame
import math

class Main:
    """Main class of the simulation"""
    def __init__(self):
        pygame.init()
        # set width, height and screen
        self.width: int = 500
        self.height: int = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Polygon Simulation")
        
        # font
        self.font = pygame.font.Font('freesansbold.ttf', 16)

        # vars for art
        self.distance = 225 # distance of the point from the center
        self.color = (111, 189, 241)
        self.num_edges = 3
        self.radius = 1

        # fps, clock and run
        self.clock = pygame.time.Clock()
        self.fps: int = 3
        self.run: bool = True
        self.run_simulation: bool = False
    
    def event(self):
        """Event Loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.run_simulation = not self.run_simulation
    
    def main(self):
        """Main Function"""
        
        while self.run:
            self.event()
            self.draw()
            self.clock.tick(self.fps)

    def angles(self, edge_num: int = 3):
        """Angles"""
        degre = 360 / edge_num
        max_degre = 0
        
        while max_degre < 360:
            max_degre += degre
            yield max_degre
    
    def draw_circles(self, x1, y1):
        for angle in self.angles(self.num_edges):
            (x2,y2) = (x1 + self.distance*math.cos(math.radians(angle)),y1 + self.distance*math.sin(math.radians(angle)))
            self.positions.append((x2, y2))
            pygame.draw.circle(self.screen, self.color, (x2, y2), self.radius)
    
    def draw_lines(self):
        for index, pos1 in enumerate(self.positions):
            for pos2 in self.positions[index:]:
                pygame.draw.line(self.screen, self.color, pos1, pos2, self.radius)
    
    def draw(self):
        """Main Draw Funciton"""
        self.screen.fill((0, 0, 0))

        x1, y1 = 250, 250
        pygame.draw.circle(self.screen, self.color, (x1, y1), self.radius)
        
        self.positions = [(x1, y1)]
        self.draw_circles(x1, y1)
        self.draw_lines()
        
        text = self.font.render(str(self.num_edges), True, self.color)
        self.screen.blit(text, (10, 10))

        if self.run_simulation:
            self.num_edges += 1
        pygame.display.flip()

Main().main()