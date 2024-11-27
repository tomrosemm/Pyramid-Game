import unittest
from Entrance import Entrance # type: ignore

class EntranceTest(unittest.TestCase):

    def test_deposit(self):
        cls = Entrance(player, roomStates)
        self.assertTrue(cls(player["hasTorch"], roomStates), "should be true")

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
    unittest.main()
    Entrance(player, roomStates)