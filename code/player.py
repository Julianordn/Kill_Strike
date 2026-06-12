#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity


class Player(Entity):

    def __init__(self):

        surf = pygame.image.load(
            "./asset/Attacck.png"
        )

        rect = surf.get_rect(
            center=(400, 300)
        )

        super().__init__(
            "Player",
            surf,
            rect
        )

        self.direction = "RIGHT"
        self.speed = 5


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