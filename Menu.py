import pygame

class Menu:

    def get_center_x(self, text):
        return self.screen.get_rect().width / 2 - text.get_rect().width / 2

    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        self.color = (0, 0, 0)

        self.header_font = pygame.font.SysFont("orange juice", 140)
        self.start_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.help_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.about_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.quit_font = pygame.font.SysFont("Comic Sans MS", 60)

        self.header_text = self.header_font.render("TypeZ", True, self.color)
        self.start_text = self.start_font.render("Start", True, self.color)
        self.help_text = self.help_font.render("Help", True, self.color)
        self.about_text = self.about_font.render("About", True, self.color)
        self.quit_text = self.quit_font.render("Quit", True, self.color)

        self.start_button = self.start_text.get_rect(x=self.get_center_x(self.start_text), y=230)
        self.help_button = self.help_text.get_rect(x=self.get_center_x(self.help_text), y=305)
        self.about_button = self.about_text.get_rect(x=self.get_center_x(self.about_text), y=380)
        self.quit_button = self.about_text.get_rect(x=self.get_center_x(self.quit_text), y=455)

    def loop(self):
        for event in pygame.event.get():
            if self.quit_button.collidepoint(self.game.get_mpos()):
                self.quit_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.stop_game()
            else:
                self.quit_font = pygame.font.SysFont("Comic Sans MS", 60)

            if self.start_button.collidepoint(self.game.get_mpos()):
                self.start_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.change_level(1)
            else:
                self.start_font = pygame.font.SysFont("Comic Sans MS", 60)

            if self.help_button.collidepoint(self.game.get_mpos()):
                self.help_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.change_level(2)
            else:
                self.help_font = pygame.font.SysFont("Comic Sans MS", 60)

            if self.about_button.collidepoint(self.game.get_mpos()):
                self.about_font = pygame.font.SysFont("Comic Sans MS", 66)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.change_level(3)
            else:
                self.about_font = pygame.font.SysFont("Comic Sans MS", 60)

            if event.type == pygame.QUIT:
                self.game.stop_game()

    def draw(self):
        self.start_text = self.start_font.render("Start", True, self.color)
        self.help_text = self.help_font.render("Help", True, self.color)
        self.about_text = self.about_font.render("About", True, self.color)
        self.quit_text = self.quit_font.render("Quit", True, self.color)

        self.screen.blit(self.header_text, (self.get_center_x(self.header_text), 70))
        self.screen.blit(self.start_text, self.start_button)
        self.screen.blit(self.help_text, self.help_button)
        self.screen.blit(self.about_text, self.about_button)
        self.screen.blit(self.quit_text, self.quit_button)
