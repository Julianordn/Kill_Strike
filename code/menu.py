#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:

    def __init__(self, window):
        self.window = window

        self.surf = pygame.image.load("./asset/War.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        pygame.mixer.music.load("./asset/war.mp3.wav")
        pygame.mixer.music.play(-1)

        while True:

            # Desenha fundo
            self.window.blit(
                source=self.surf,
                dest=self.rect
            )

            # Título
            self.menu_text(
                text_size=100,
                text="KILL",
                text_color=(128, 0, 32),
                text_center_pos=(WIN_WIDTH / 2, 70)
            )

            self.menu_text(
                text_size=100,
                text="STRIKE",
                text_color=(128, 0, 32),
                text_center_pos=(WIN_WIDTH / 2, 170)
            )

            # Objetivo
            self.menu_text(
                text_size=30,
                text="ELIMINE 30 INIMIGOS PARA VENCER",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 280)
            )

            # Controles
            self.menu_text(
                text_size=25,
                text="CONTROLES",
                text_color=(255, 255, 0),
                text_center_pos=(WIN_WIDTH / 2, 340)
            )

            self.menu_text(
                text_size=20,
                text="W - MOVER PARA CIMA",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 390)
            )

            self.menu_text(
                text_size=20,
                text="S - MOVER PARA BAIXO",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 420)
            )

            self.menu_text(
                text_size=20,
                text="A - MOVER PARA ESQUERDA",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 450)
            )

            self.menu_text(
                text_size=20,
                text="D - MOVER PARA DIREITA",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 480)
            )

            self.menu_text(
                text_size=20,
                text="ESPACO - ATIRAR",
                text_color=(255, 255, 255),
                text_center_pos=(WIN_WIDTH / 2, 510)
            )

            self.menu_text(
                text_size=25,
                text="ENTER - INICIAR MISSAO",
                text_color=(0, 255, 0),
                text_center_pos=(WIN_WIDTH / 2, 570)
            )

            pygame.display.flip()

            # Eventos
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
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
            name="Impact",
            size=text_size
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
            source=text_surf,
            dest=text_rect
        )