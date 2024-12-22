import unittest
from Encampment import Encampment # type: ignore

class EncampmentTest(unittest.TestCase):

    def test_Encampment(self):
        cls = Encampment(player, roomStates)
        self.assertTrue(cls(player, roomStates["Encampmemnt"]["battleWon"]), "should be true")

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
    Encampment(player, roomStates)
    unittest.main()