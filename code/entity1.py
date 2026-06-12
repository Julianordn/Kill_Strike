#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from pygame import Surface, Rect


class Entity(ABC):

    def __init__(self, name: str, surf: Surface, rect: Rect):

        self.name = name
        self.surf = surf
        self.rect = rect


    @abstractmethod
    def move(self):

        pass


    def draw(self, window):

        window.blit(
            source=self.surf,
            dest=self.rect
        )