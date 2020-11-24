import sys
import pygame
from settings import Settings
from space_ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game. and create game resourcess."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Venom's First Python Game")

        self.ship = Ship(self)

        # Set the background color.

    def _check_events(self):
        """Respond to keypress and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.rect.x += 9
                elif event.key == pygame.K_LEFT:
                    #Move the ship to the right
                    self.ship.rect.x -= 9

    def _update_screen(self):
        """Update umages on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()


    def run_game(self):
        """Start the main loop for the game. """
        while True:

            self._check_events()
            self._update_screen()


            #Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Male a game isntance, and run the game.
    ai = AlienInvasion()
    ai.run_game()