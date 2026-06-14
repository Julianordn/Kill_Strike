#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_type: str):

        entity_list = []


        # ==========================
        # CRIAR PLAYER
        # ==========================

        if entity_type == "PLAYER":

            entity_list.append(
                Player()
            )


        # ==========================
        # CRIAR INIMIGOS
        # ==========================

        elif entity_type == "ENEMY":

            positions = [

                (50, 50),

                (750, 50),

                (50, 580),

                (750, 580),

                (400, 50),

                (400, 580)

            ]

            for pos in positions:
                entity_list.append(

                    Enemy(

                        pos[0],

                        pos[1]

                    )

                )


        return entity_list