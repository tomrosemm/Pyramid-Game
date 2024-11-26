import unittest
from Armory import Armory # type: ignore

class ArmoryTest(unittest.TestCase):

    def test_Armory(self):
        cls = Armory()
        self.assertTrue(cls.player["hasSword"], "player doesn't have sword")

if __name__ == '__main__':
    
    player = {
        "name": "TestPlayer",
        "health": 100,
        "baseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    roomStates = {}
    
    unittest.Armory(player, roomStates)