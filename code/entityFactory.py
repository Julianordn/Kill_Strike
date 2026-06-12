#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_type: str):

        entity_list = []

        if entity_type == "PLAYER":

            entity_list.append(
                Player()
            )

        elif entity_type == "ENEMY":

            positions = [

                (50, 50),
                (150, 50),
                (250, 50),
                (350, 50),
                (450, 50),
                (550, 50),

                (50, 150),
                (150, 150),
                (250, 150),
                (350, 150),
                (450, 150),
                (550, 150),

                (50, 250),
                (150, 250),
                (250, 250),
                (350, 250),
                (450, 250),
                (550, 250),

                (50, 350),
                (150, 350),
                (250, 350),
                (350, 350),
                (450, 350),
                (550, 350),

                (50, 450),
                (150, 450),
                (250, 450),
                (350, 450),
                (450, 450),
                (550, 450)

            ]

            for pos in positions:

                entity_list.append(
                    Enemy(
                        pos[0],
                        pos[1]
                    )
                )

        return entity_list