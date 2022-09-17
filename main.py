import pygame
from sprites import *
from config import *
import sys


class Game:
    def __init__(self):
        """Initialize pygame and screen."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, col in enumerate(row):
                Ground(self, j, i)
                if col == "B":
                    Block(self, j, i)
                if col == "E":
                    Enemy(self, j, i)
                if col == "P":
                    Player(self, j, i)

    def new(self):
        """Starts a new game for the player."""
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        """Game loop events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        """Game loop updates."""
        self.all_sprites.update()

    def draw(self):
        """Game loop draw."""
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        """Game loop."""
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
        pass

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()
