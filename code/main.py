import pygame
import sys
from settings import *  # Ensure settings.py exists and contains the required constants.

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Platformer')
        self.clock = pygame.time.Clock()
        self.running = True

        # Groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

    def handle_events(self):
        """Handles user input and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt):
        """Updates game objects."""
        self.all_sprites.update(dt)

    def draw(self):
        """Draws objects on the screen."""
        self.display_surface.fill(BG_COLOR)
        self.all_sprites.draw(self.display_surface)
        pygame.display.update()

    def run(self):
        """Main game loop."""
        while self.running:
            dt = self.clock.tick(FRAMERATE) / 1000  # Delta time for smooth movement

            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
