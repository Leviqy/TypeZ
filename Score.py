import pygame
import Ingame


class Score:
    def get_center_x(self, text):
        return self.screen.get_rect().width / 2 - text.get_rect().width / 2

    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        self.color = (0, 0, 0)

        self.score_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.menu_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.retry_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.quit_font = pygame.font.SysFont("Comic Sans MS", 60)

        self.score_text = self.score_font.render("0", True, self.color)
        self.menu_text = self.menu_font.render("Menu", True, self.color)
        self.retry_text = self.retry_font.render("Retry", True, self.color)
        self.quit_text = self.quit_font.render("Quit", True, self.color)

        self.menu_button = self.menu_text.get_rect(x=self.get_center_x(self.menu_text), y=205)
        self.retry_button = self.retry_text.get_rect(x=self.get_center_x(self.retry_text), y=305)
        self.quit_button = self.quit_text.get_rect(x=self.get_center_x(self.quit_text), y=405)

    def loop(self):
        for event in pygame.event.get():
            if self.quit_button.collidepoint(self.game.get_mpos()):
                self.quit_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.stop_game()
            else:
                self.quit_font = pygame.font.SysFont("Comic Sans MS", 60)

            if self.menu_button.collidepoint(self.game.get_mpos()):
                self.menu_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.change_level(0)
            else:
                self.menu_font = pygame.font.SysFont("Comic Sans MS", 60)

            if self.retry_button.collidepoint(self.game.get_mpos()):
                self.retry_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.change_level(1)
            else:
                self.retry_font = pygame.font.SysFont("Comic Sans MS", 60)

            if event.type == pygame.QUIT:
                self.game.stop_game()

    def draw(self):
        self.score_text = self.score_font.render(str(Ingame.Ingame.get_last_score()), True, self.color)
        self.menu_text = self.menu_font.render("Menu", True, self.color)
        self.retry_text = self.retry_font.render("Retry", True, self.color)
        self.quit_text = self.quit_font.render("Quit", True, self.color)

        self.menu_button = self.menu_text.get_rect(x=self.get_center_x(self.menu_text), y=205)
        self.retry_button = self.retry_text.get_rect(x=self.get_center_x(self.retry_text), y=305)
        self.quit_button = self.quit_text.get_rect(x=self.get_center_x(self.quit_text), y=405)

        self.screen.blit(self.score_text, (self.get_center_x(self.score_text), 100))
        self.screen.blit(self.menu_text, self.menu_button)
        self.screen.blit(self.retry_text, self.retry_button)
        self.screen.blit(self.quit_text, self.quit_button)
