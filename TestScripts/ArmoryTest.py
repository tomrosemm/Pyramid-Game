import unittest
from Armory import Armory # type: ignore

class ArmoryTest(unittest.TestCase):

    def test_Armory(self):
        cls = Armory(player, roomStates)
        self.assertTrue(cls(player["hasSword"], roomStates), "should be true")

if __name__ == '__main__':
    
    player = {
        "name": "TestPlayer",
        "maxHealth": 100,
        "health": 100,
        "baseDamageRange": (10,20),
        "originalBaseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }
    
    roomStates = {}
    Armory(player, roomStates)
    unittest.main()