# A typing game that shows off your typing accuracy and speed
# Made by @Leviqy

import pygame
import Menu
import Ingame
import Score
import Instructions
import About

running = True
level = 0
mpos = 0, 0


class Game:

    @staticmethod
    def change_level(state):
        global level
        level = state

    @staticmethod
    def get_mpos():
        global mpos
        return mpos

    @staticmethod
    def stop_game():
        global running
        running = False

    def main(self):

        global mpos
        global running
        global level

        pygame.font.init()
        pygame.init()

        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("img//TypeZ")

        menu = Menu.Menu(self, screen)
        ingame = Ingame.Ingame(self, screen)
        score = Score.Score(self, screen)
        instructions = Instructions.Instructions(self, screen)
        about = About.About(self, screen)

        background = pygame.image.load("img//notebook.png")

        framerate = pygame.time.Clock()

        while running:
            framerate.tick(60)
            mpos = pygame.mouse.get_pos()

            screen.blit(background, (0, 0))

            if level == 0:
                menu.loop()
                menu.draw()
            elif level == 1:
                ingame.loop()
                ingame.draw()
            elif level == 2:
                instructions.loop()
                instructions.draw()
            elif level == 3:
                about.loop()
                about.draw()
            elif level == 4:
                score.loop()
                score.draw()

            pygame.display.flip()


if __name__ == "__main__":
    Game().main()
