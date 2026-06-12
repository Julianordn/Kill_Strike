#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, x, y):

        surf = pygame.image.load(
            "./asset/terrorist.png"
        )

        rect = surf.get_rect(
            center=(x, y)
        )

        super().__init__(
            "Enemy",
            surf,
            rect
        )

        self.speed = 2
        self.direction = 1


    def move(self):

        self.rect.x += self.speed * self.direction

        if self.rect.right >= 800:
            self.direction = -1

        if self.rect.left <= 0:
            self.direction = 1