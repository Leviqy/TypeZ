import pygame
import random


class Ingame:
    last_score = 0

    def get_center_x(self, text):
        return self.screen.get_rect().width / 2 - text.get_rect().width / 2

    def pick_word(self):
        rand = random.randint(0, len(self.word_list) - 1)
        return self.word_list[rand]

    @staticmethod
    def cut_first_char(word):
        return word[1:]

    @staticmethod
    def get_last_score():
        global last_score
        return last_score

    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

        self.color = (0, 0, 0)

        self.points = 0
        self.countdown = 3
        self.invincible = 0
        self.timer = 3

        self.word_list = [
            "freedom",
            "soda",
            "reading",
            "writing",
            "question",
            "conclusion",
            "challenge",
            "fun",
            "understanding",
            "literature",
            "internet",
            "television",
            "development",
            "management",
            "language",
            "exam",
            "direction",
            "department",
            "marriage",
            "communication",
            "disease",
            "advertising",
            "entertainment",
            "competition",
            "context",
            "performance",
            "newspaper",
            "appearance",
            "expression",
            "administration",
            "possession",
            "interaction",
            "atmosphere",
            "construction",
            "refrigerator",
            "measurement",
            "appointment",
            "manufacturer",
            "establishment",
        ]

        self.game_font = pygame.font.SysFont("Comic Sans MS", 60)
        self.word = self.pick_word()
        self.curr_word = self.word

        self.timerclock = 0
        self.invincibleclock = 0
        self.countdownclock = 0

        self.dword = self.game_font.render(self.word, True, self.color)
        self.dpoints = self.game_font.render(str(self.points), True, self.color)
        self.dtimer = self.game_font.render(str(self.timer), True, self.color)
        self.dcountdown = self.game_font.render(str(self.countdown), True, self.color)

        self.center_x = self.screen.get_rect().width / 2 - self.dword.get_rect().width / 2

    def loop(self):
        global last_score

        if self.countdown > 0:
            self.countdownclock += 1
            if self.countdownclock >= 60:
                self.countdownclock = 0
                self.countdown -= 1
        else:
            self.center_x = self.screen.get_rect().width / 2 - self.dword.get_rect().width / 2
            self.timerclock += 1

            if self.invincible > 0:
                self.invincibleclock += 1
                if self.invincibleclock >= 30:
                    self.invincible = 0
                    self.invincibleclock = 0

            if self.timerclock >= 60:
                self.timer -= 1
                self.timerclock = 0

            if self.timer <= 0:
                last_score = self.points
                self.__init__(self.game, self.screen)
                self.game.change_level(4)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if chr(event.key) == self.word[0]:
                        self.word = self.cut_first_char(self.word)
                        self.center_x = self.screen.get_rect().width / 2 - self.dword.get_rect().width / 2
                        if len(self.word) == 0:
                            self.word = self.pick_word()
                            self.curr_word = self.word
                            self.points += 1
                            self.timer += 2
                    elif self.invincible == 0:
                        self.word = self.curr_word
                        self.timer -= 2
                        self.invincible += 1

                if event.type == pygame.QUIT:
                    self.game.stop_game()

    def draw(self):
        if self.countdown > 0:
            self.dcountdown = self.game_font.render(str(self.countdown), True, self.color)
            self.screen.blit(self.dcountdown, (self.get_center_x(self.dcountdown), 245))
        else:
            self.dword = self.game_font.render(self.word, True, self.color)
            self.dpoints = self.game_font.render(str(self.points), True, self.color)
            self.dtimer = self.game_font.render(str(self.timer), True, self.color)

            self.screen.blit(self.dword, (self.get_center_x(self.dword), 280))
            self.screen.blit(self.dtimer, (700, 20))
            self.screen.blit(self.dpoints, (20, 20))
