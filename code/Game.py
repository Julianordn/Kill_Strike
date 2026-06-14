#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.Level import Level



class Game:


    def __init__(self):

        pygame.init()

        pygame.mixer.init()


        self.window = pygame.display.set_mode(
            (
                WIN_WIDTH,
                WIN_HEIGHT
            )
        )


        pygame.display.set_caption(
            "KILL STRIKE"
        )



    def run(self):


        while True:


            menu = Menu(
                self.window
            )


            result = menu.run()



            if result == "START":


                # LEVEL 1

                level1 = Level(

                    self.window,

                    "Level 1",

                    "NORMAL",

                    "./asset/War1.png",

                    30

                )


                level1.run()



                # LEVEL 2

                level2 = Level(

                    self.window,

                    "Level 2",

                    "NORMAL",

                    "./asset/War2.png",

                    40

                )


                level2.run()



                # LEVEL 3

                level3 = Level(

                    self.window,

                    "Level 3",

                    "HARD",

                    "./asset/War3.png",

                    50

                )


                level3.run()



                # FINAL

                self.show_final_message()



    def show_final_message(self):


        self.window.fill(
            (0,0,0)
        )


        font = pygame.font.SysFont(
            "Impact",
            80
        )


        text = font.render(
            "VOCÊ VENCEU!",
            True,
            (0,255,0)
        )


        rect = text.get_rect(
            center=(
                WIN_WIDTH//2,
                WIN_HEIGHT//2
            )
        )


        self.window.blit(
            text,
            rect
        )


        pygame.display.flip()


        pygame.time.wait(
            5000
        )