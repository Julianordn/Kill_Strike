#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:


    def __init__(self, window):

        self.window = window

        self.surf = pygame.image.load(
            "./asset/War.png"
        )

        self.rect = self.surf.get_rect(
            left=0,
            top=0
        )



    def run(self):


        pygame.mixer.music.load(
            "./asset/war.mp3.wav"
        )

        pygame.mixer.music.play(-1)


        # limpa qualquer tecla/evento antigo

        pygame.event.clear()



        while True:


            self.window.blit(

                self.surf,

                self.rect

            )



            # TÍTULO


            self.menu_text(

                100,

                "KILL",

                (128,0,32),

                (WIN_WIDTH / 2,80)

            )


            self.menu_text(

                100,

                "STRIKE",

                (128,0,32),

                (WIN_WIDTH / 2,170)

            )



            # OBJETIVO

            self.menu_text(
                text_size=30,
                text="COMPLETE 3 NIVEIS E ELIMINE TODOS OS INIMIGOS",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 280)
            )



            # CONTROLES


            self.menu_text(

                30,

                "CONTROLES",

                (255,255,0),

                (WIN_WIDTH / 2,340)

            )



            self.menu_text(

                20,

                "W - MOVER PARA CIMA",

                (255,255,255),

                (WIN_WIDTH / 2,390)

            )


            self.menu_text(

                20,

                "S - MOVER PARA BAIXO",

                (255,255,255),

                (WIN_WIDTH / 2,420)

            )


            self.menu_text(

                20,

                "A - MOVER PARA ESQUERDA",

                (255,255,255),

                (WIN_WIDTH / 2,450)

            )


            self.menu_text(

                20,

                "D - MOVER PARA DIREITA",

                (255,255,255),

                (WIN_WIDTH / 2,480)

            )


            self.menu_text(

                20,

                "ESPACO - ATIRAR",

                (255,255,255),

                (WIN_WIDTH / 2,510)

            )



            self.menu_text(

                25,

                "ENTER - INICIAR MISSAO",

                (0,255,0),

                (WIN_WIDTH / 2,570)

            )



            pygame.display.flip()



            for event in pygame.event.get():



                if event.type == pygame.QUIT:

                    pygame.quit()

                    quit()



                if event.type == pygame.KEYDOWN:



                    if event.key == pygame.K_RETURN:



                        # limpa o ENTER antes de sair do menu

                        pygame.event.clear()


                        pygame.mixer.music.stop()


                        return "START"







    def menu_text(

            self,

            text_size: int,

            text: str,

            text_color: tuple,

            text_center_pos: tuple

    ):



        text_font: Font = pygame.font.SysFont(

            "Impact",

            text_size

        )



        text_surf: Surface = text_font.render(

            text,

            True,

            text_color

        ).convert_alpha()



        text_rect: Rect = text_surf.get_rect(

            center=text_center_pos

        )



        self.window.blit(

            text_surf,

            text_rect

        )