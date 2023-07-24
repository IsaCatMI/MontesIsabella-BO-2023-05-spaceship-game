from game.components.power_ups.power_up import PowerUp

from game.utils.constants import SHIELD1, SHIELD_1_TYPE

class Shield1(PowerUp):
    def __init__(self):
        super().__init__(SHIELD1, SHIELD_1_TYPE)