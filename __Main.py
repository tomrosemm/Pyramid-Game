#Import rooms
import _Entrance
#Encampment
import _SnakeWay
import _SphinxRoom
#Armory
import _InnerBurialChamber
import _SandyCove
#Royal Tomb
#Treasure Chamber

#Import Systems
import Combat

#Import Libraries
import random
import time

player = {
    "name": "Player",
    "health": 100,
    "baseDamageRange": (10,20),
    "hasAxe": False,
    "hasSword": False,
    "axeBonus": (5, 10),
    "swordBonus": (10,15)
}

tombGoblin = {
    "name": "Goblin Fred",
    "health": 75,
    "damageRange": (5,15)
}
