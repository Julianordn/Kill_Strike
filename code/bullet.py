#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity


class Bullet(Entity):

    def __init__(self, x, y, direction):

        surf = pygame.Surface((10, 10))
        surf.fill((255, 255, 0))

        rect = surf.get_rect(
            center=(x, y)
        )

        super().__init__(
            "Bullet",
            surf,
            rect
        )

        self.direction = direction
        self.speed = 10


    def move(self):

        if self.direction == "UP":
            self.rect.y -= self.speed

        elif self.direction == "DOWN":
            self.rect.y += self.speed

        elif self.direction == "LEFT":
            self.rect.x -= self.speed

        elif self.direction == "RIGHT":
            self.rect.x += self.speed