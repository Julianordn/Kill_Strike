#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Bullet import Bullet
from code.Player import Player
from code.Enemy import Enemy


class Level:

    def __init__(self, window, name, game_mode):

        self.window = window
        self.name = name
        self.game_mode = game_mode

        self.background = pygame.image.load(
            "./asset/War1.png"
        )

        self.entity_list: list[Entity] = []

        self.entity_list.extend(
            EntityFactory.get_entity("PLAYER")
        )

        self.entity_list.extend(
            EntityFactory.get_entity("ENEMY")
        )

        self.kills = 0
        self.target_kills = 30

        self.font = pygame.font.SysFont(
            "Arial",
            30
        )

    def run(self):

        clock = pygame.time.Clock()

        while True:

            # =========================
            # EVENTOS
            # =========================

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        player = None

                        for ent in self.entity_list:

                            if isinstance(ent, Player):
                                player = ent
                                break

                        if player:

                            bullet = Bullet(
                                player.rect.centerx,
                                player.rect.centery,
                                player.direction
                            )

                            self.entity_list.append(
                                bullet
                            )

            # =========================
            # DESENHAR FUNDO
            # =========================

            self.window.blit(
                self.background,
                (0, 0)
            )

            # =========================
            # MOVIMENTO E DESENHO
            # =========================

            for ent in self.entity_list[:]:

                ent.move()

                ent.draw(
                    self.window
                )

            # =========================
            # COLISÃO BALA X INIMIGO
            # =========================

            bullets = [
                ent for ent in self.entity_list
                if isinstance(ent, Bullet)
            ]

            enemies = [
                ent for ent in self.entity_list
                if isinstance(ent, Enemy)
            ]

            for bullet in bullets:

                for enemy in enemies:

                    if bullet.rect.colliderect(
                            enemy.rect):

                        if bullet in self.entity_list:
                            self.entity_list.remove(
                                bullet
                            )

                        if enemy in self.entity_list:
                            self.entity_list.remove(
                                enemy
                            )

                        self.kills += 1

                        break

            # =========================
            # DERROTA
            # =========================

            player = None

            for ent in self.entity_list:

                if isinstance(ent, Player):
                    player = ent
                    break

            if player:

                for enemy in enemies:

                    if player.rect.colliderect(
                            enemy.rect):

                        self.show_message(
                            "GAME OVER",
                            (255, 0, 0)
                        )

                        return

            # =========================
            # VITÓRIA
            # =========================

            if self.kills >= self.target_kills:

                self.show_message(
                    "MISSION COMPLETE",
                    (0, 255, 0)
                )

                return

            # =========================
            # HUD
            # =========================

            kills_text = self.font.render(
                f"Kills: {self.kills}/{self.target_kills}",
                True,
                (255, 255, 255)
            )

            self.window.blit(
                kills_text,
                (20, 20)
            )

            pygame.display.flip()

            clock.tick(60)

    def show_message(self, text, color):

        self.window.blit(
            self.background,
            (0, 0)
        )

        font = pygame.font.SysFont(
            "Impact",
            80
        )

        text_surf = font.render(
            text,
            True,
            color
        )

        text_rect = text_surf.get_rect(
            center=(
                self.window.get_width() // 2,
                self.window.get_height() // 2
            )
        )

        self.window.blit(
            text_surf,
            text_rect
        )

        pygame.display.flip()

        pygame.time.wait(3000)