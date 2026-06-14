#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Bullet import Bullet
from code.Player import Player
from code.Enemy import Enemy


class Level:


    def __init__(self, window, name, game_mode, background, target_kills):

        self.window = window

        self.name = name

        self.game_mode = game_mode


        # Música da fase

        pygame.mixer.music.load(
            "./asset/level_music.wav"
        )

        pygame.mixer.music.play(-1)



        # Fundo

        self.background = pygame.image.load(
            background
        )

        self.background = pygame.transform.scale(
            self.background,
            (WIN_WIDTH, WIN_HEIGHT)
        )



        # Entidades

        self.entity_list: list[Entity] = []



        self.entity_list.extend(
            EntityFactory.get_entity("PLAYER")
        )



        self.entity_list.extend(
            EntityFactory.get_entity("ENEMY")
        )



        # Sistema de pontuação

        self.kills = 0

        self.target_kills = target_kills


        self.enemy_spawned = 5



        self.font = pygame.font.SysFont(
            "Arial",
            30
        )

        self.show_level_intro()



    def run(self):

        clock = pygame.time.Clock()



        while True:



            # ======================
            # EVENTOS
            # ======================

            for event in pygame.event.get():


                if event.type == pygame.QUIT:

                    pygame.quit()
                    quit()



                if event.type == pygame.KEYDOWN:


                    if event.key == pygame.K_SPACE:


                        player = self.get_player()


                        if player:


                            bullet = Bullet(

                                player.rect.centerx,

                                player.rect.centery,

                                player.direction

                            )


                            self.entity_list.append(
                                bullet
                            )





            # ======================
            # DESENHA FUNDO
            # ======================

            self.window.blit(

                self.background,

                (0,0)

            )




            # ======================
            # MOVIMENTO ENTIDADES
            # ======================


            player = self.get_player()



            for entity in self.entity_list[:]:


                if isinstance(entity, Enemy):

                    entity.move(
                        player
                    )


                else:

                    entity.move()



                if isinstance(entity, Bullet):


                    if entity.is_offscreen():


                        self.entity_list.remove(
                            entity
                        )

                        continue



                entity.draw(
                    self.window
                )






            # ======================
            # COLISÕES
            # ======================


            self.check_bullet_collision()


            self.check_player_collision()






            # ======================
            # VITÓRIA
            # ======================

            if self.kills >= self.target_kills:


                self.show_message(

                    "MISSION COMPLETE",

                    (0,255,0)

                )


                return





            # ======================
            # HUD
            # ======================


            kills_text = self.font.render(

                f"KILLS: {self.kills}/{self.target_kills}",

                True,

                (255,255,255)

            )



            self.window.blit(

                kills_text,

                (20,20)

            )



            self.draw_health_bar()



            pygame.display.flip()


            clock.tick(60)







    def get_player(self):


        for entity in self.entity_list:


            if isinstance(entity, Player):

                return entity



        return None






    def spawn_enemy(self):


        positions = [


            (80,80),

            (700,80),

            (80,500),

            (700,500),

            (400,100)


        ]



        pos = positions[

            self.enemy_spawned % len(positions)

        ]



        enemy = Enemy(

            pos[0],

            pos[1]

        )


        self.entity_list.append(

            enemy

        )


        self.enemy_spawned += 1






    def check_bullet_collision(self):


        bullets = [

            entity for entity in self.entity_list

            if isinstance(entity, Bullet)

        ]



        enemies = [

            entity for entity in self.entity_list

            if isinstance(entity, Enemy)

        ]



        for bullet in bullets:


            for enemy in enemies:



                if bullet.rect.colliderect(

                    enemy.rect

                ):



                    if bullet in self.entity_list:

                        self.entity_list.remove(
                            bullet
                        )



                    if enemy in self.entity_list:

                        self.entity_list.remove(
                            enemy
                        )



                    self.kills += 1



                    if self.kills < self.target_kills:

                        self.spawn_enemy()



                    break






    def check_player_collision(self):


        player = self.get_player()



        if player:


            for enemy in self.entity_list:


                if isinstance(enemy, Enemy):


                    if player.rect.colliderect(

                        enemy.rect

                    ):



                        player.health -= 1



                        enemy.rect.x += 80



                        if player.health <= 0:


                            self.show_message(

                                "GAME OVER",

                                (255,0,0)

                            )


                            pygame.quit()

                            quit()






    def draw_health_bar(self):


        player = self.get_player()



        if player:



            bar_width = 200

            bar_height = 20



            health_width = (

                player.health / 100

            ) * bar_width





            pygame.draw.rect(

                self.window,

                (150,0,0),

                (

                    20,

                    60,

                    bar_width,

                    bar_height

                )

            )





            pygame.draw.rect(

                self.window,

                (0,255,0),

                (

                    20,

                    60,

                    health_width,

                    bar_height

                )

            )





            health_text = self.font.render(

                f"VIDA: {player.health}",

                True,

                (255,255,255)

            )



            self.window.blit(

                health_text,

                (20,85)

            )

    def show_level_intro(self):

        self.window.blit(
            self.background,
            (0, 0)
        )

        font_title = pygame.font.SysFont(
            "Impact",
            90
        )

        font_text = pygame.font.SysFont(
            "Arial",
            35
        )

        title = font_title.render(
            self.name.upper(),
            True,
            (255, 0, 0)
        )

        mission = font_text.render(
            f"ELIMINE {self.target_kills} INIMIGOS",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(
                WIN_WIDTH // 2,
                WIN_HEIGHT // 2 - 50
            )
        )

        mission_rect = mission.get_rect(
            center=(
                WIN_WIDTH // 2,
                WIN_HEIGHT // 2 + 40
            )
        )

        self.window.blit(
            title,
            title_rect
        )

        self.window.blit(
            mission,
            mission_rect
        )

        pygame.display.flip()

        pygame.time.wait(
            2000
        )




    def show_message(self, text, color):


        self.window.blit(

            self.background,

            (0,0)

        )



        font = pygame.font.SysFont(

            "Impact",

            80

        )



        text_surface = font.render(

            text,

            True,

            color

        )



        text_rect = text_surface.get_rect(

            center=(

                WIN_WIDTH // 2,

                WIN_HEIGHT // 2

            )

        )



        self.window.blit(

            text_surface,

            text_rect

        )



        pygame.display.flip()



        pygame.time.wait(3000)