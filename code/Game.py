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



            # MENU

            menu = Menu(

                self.window

            )



            result = menu.run()



            # INICIA O LEVEL


            if result == "START":



                level = Level(

                    self.window,

                    "Level 1",

                    "NORMAL"

                )



                level.run()