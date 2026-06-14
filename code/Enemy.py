#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, x, y):

        surf = pygame.image.load(
            "./asset/enemy.png"
        )


        surf = pygame.transform.scale(
            surf,
            (60,60)
        )


        rect = surf.get_rect(
            center=(x,y)
        )


        super().__init__(
            "Enemy",
            surf,
            rect
        )


        self.speed = 2

        # controle de ataque
        self.attack_cooldown = 500

        self.last_attack = 0



    def move(self, player):


        if player.rect.x > self.rect.x:

            self.rect.x += self.speed


        elif player.rect.x < self.rect.x:

            self.rect.x -= self.speed



        if player.rect.y > self.rect.y:

            self.rect.y += self.speed


        elif player.rect.y < self.rect.y:

            self.rect.y -= self.speed



    def can_attack(self):

        current_time = pygame.time.get_ticks()


        if current_time - self.last_attack >= self.attack_cooldown:

            self.last_attack = current_time

            return True


        return False