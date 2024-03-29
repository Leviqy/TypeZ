import pygame


class Instructions:

    def get_center_x(self, text):
        return self.screen.get_rect().width / 2 - text.get_rect().width / 2

    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        self.instructions = pygame.image.load("img/instruction.png")
        self.instructions.convert_alpha()

        self.color = (0, 0, 0)

        self.back_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.back_text = self.back_font.render("Back", True, self.color)
        self.back_button = self.back_text.get_rect(x=self.get_center_x(self.back_text), y=480)

    def loop(self):
        for event in pygame.event.get():
            if self.back_button.collidepoint(self.game.get_mpos()):
                self.back_font = pygame.font.SysFont("Comic Sans MS", 65)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.game.change_level(0)
            else:
                self.back_font = pygame.font.SysFont("Comic Sans MS", 60)

            if event.type == pygame.QUIT:
                self.game.stop_game()


    def draw(self):
        self.back_text = self.back_font.render("Back", True, self.color)

        self.screen.blit(self.instructions, (80,70))
        self.screen.blit(self.back_text, self.back_button)
