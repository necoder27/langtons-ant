import pygame 
import random

pygame.init()

SCREEN_HEIGHT = 1080 
SCREEN_WIDTH = 1920
TILE_SIZE = 10
FPS = 120

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()

class Ant:
    def __init__(self):
        self.pos_x = random.randrange(0, SCREEN_WIDTH // TILE_SIZE)
        self.pos_y = random.randrange(0, SCREEN_HEIGHT // TILE_SIZE)
        self.movement = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])

    def turn_left(self):
        x, y = self.movement
        self.movement = (y, -x)

    def turn_right(self):
        x, y = self.movement
        self.movement = (-y, x)

    def generate_step(self, white_tiles):
        current_pos = (self.pos_x, self.pos_y)

        if current_pos in white_tiles:
            self.turn_right()
            white_tiles.remove(current_pos)
        else:
            self.turn_left()
            white_tiles.add(current_pos)

        self.pos_x += self.movement[0]
        self.pos_y += self.movement[1]

        self.pos_x %= (SCREEN_WIDTH // TILE_SIZE)
        self.pos_y %= (SCREEN_HEIGHT // TILE_SIZE)

    def draw_step(self, white_tiles):
        for pos in white_tiles:
            pygame.draw.rect(screen, pygame.Color("white"), (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def main():
    running = True
    ant = Ant()
    white_tiles = {(ant.pos_x, ant.pos_y)}

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        screen.fill(pygame.Color("black"))
        ant.generate_step(white_tiles)
        ant.draw_step(white_tiles)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
