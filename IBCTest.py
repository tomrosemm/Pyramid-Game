import unittest
from InnerBurialChamber import InnerBurialChamber # type: ignore

class InnerBurialChamberTest(unittest.TestCase):

    def test_InnerBurialChamber(self):
        cls = InnerBurialChamber(player, roomStates)
        self.assertTrue(cls(player, roomStates["InnerBurialChamber"]["battleWon"]), "should be true")

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
    InnerBurialChamber(player, roomStates)
    unittest.main()