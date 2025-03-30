import random
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(name=f"Level1Bg{i}", position=(0, 0)))
                    list_bg.append(Background(name=f"Level1Bg{i}", position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player(name='Player1', position=(10, WIN_HEIGHT / 2 -30))
            case 'Player2':
                return Player(name='Player2', position=(10, WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WIN_WIDTH + 10, random.randint(40, WIN_WIDTH - 40)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WIN_WIDTH + 10, random.randint(40, WIN_WIDTH - 40)))