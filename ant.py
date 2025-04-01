import pygame 
import random

pygame.init()

SCREEN_HEIGHT = 1000 
SCREEN_WIDTH = 1000
TILE_SIZE = 10
FPS = 240
THEMES = {
            "greyscale": ["black", "white", "grey52", "grey32"],
            "sakura": ["lightpink4", "lightpink", "lightpink2", "lightpink3"],
            "ice": ["lightblue4", "lightblue1", "lightblue2", "lightblue3"],
        }

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()

class Ant:
    def __init__(self):
        self.pos_x = random.randrange(0, SCREEN_WIDTH // TILE_SIZE)
        self.pos_y = random.randrange(0, SCREEN_HEIGHT // TILE_SIZE)
        self.movement = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])

    def turn_left(self):
        x, y = self.movement
        if abs(x) == abs(y):
            self.movement = (0, -y) if x == y else (-x, 0)
        self.movement = (y, -x)

    def turn_right(self):
        x, y = self.movement
        if abs(x) == abs(y):
            self.movement = (-x, 0) if x == y else (0, -y)
        self.movement = (-y, x)

    def move_diagonally(self):
        self.movement = random.choice([(-1, -1), (-1, 1), (1, -1), (1, 1)])

    def generate_step(self, colored_tiles, colors):
        current_pos = (self.pos_x, self.pos_y)

        if current_pos in colored_tiles:
            if colored_tiles[current_pos] == colors[1]:
                self.turn_right()
                colored_tiles[current_pos] = colors[2]
            elif colored_tiles[current_pos] == colors[2]:
                self.move_diagonally() # -> added diagonal movement  
                # self.turn_left() # -> traditional langton ant 
                colored_tiles[current_pos] = colors[3]
            elif colored_tiles[current_pos] == colors[3]:
                self.turn_right()
                colored_tiles.pop(current_pos)
        else:
            self.turn_left()
            colored_tiles[current_pos] = colors[1]

        self.pos_x += self.movement[0]
        self.pos_y += self.movement[1]

        self.pos_x %= (SCREEN_WIDTH // TILE_SIZE)
        self.pos_y %= (SCREEN_HEIGHT // TILE_SIZE)

    def draw_step(self, colored_tiles):
        for pos, color in colored_tiles.items():
            pygame.draw.rect(screen, pygame.Color(color), (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def main():
    running = True
    colors = THEMES["ice"]
    ant = Ant()
    colored_tiles = {(ant.pos_x, ant.pos_y): colors[1]}

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color(colors[0]))
        ant.generate_step(colored_tiles, colors)
        ant.draw_step(colored_tiles)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
