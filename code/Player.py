#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Player(Entity):

    def __init__(self):

        surf = pygame.image.load(
            "./asset/player.png"
        )
        surf = pygame.transform.scale(
            surf,
            (80, 80)
        )

        rect = surf.get_rect(
            center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)
        )

        super().__init__(
            "Player",
            surf,
            rect
        )

        self.direction = "RIGHT"
        self.speed = 5
        self.health = 100

    def move(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = "LEFT"

        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "RIGHT"

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = "UP"

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = "DOWN"

        # Limites da tela

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT