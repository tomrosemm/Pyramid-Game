import unittest
from TreasureChamber import TreasureChamber # type: ignore

class TreasureChamberTest(unittest.TestCase):

    def test_TreasureChamber(self):
        cls = TreasureChamber(player, roomStates)
        self.assertTrue(cls(player, roomStates["TreasureChamber"]["treasureTaken"]), "should be true")

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
    TreasureChamber(player, roomStates)
    unittest.main()