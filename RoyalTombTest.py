import unittest
from RoyalTomb import RoyalTomb # type: ignore

class RoyalTombTest(unittest.TestCase):

    def test_RoyalTomb(self):
        cls = RoyalTomb(player, roomStates)
        self.assertTrue(cls(player, roomStates["RoyalTomb"]["battleWon"]), "should be true")

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
    RoyalTomb(player, roomStates)
    unittest.main()