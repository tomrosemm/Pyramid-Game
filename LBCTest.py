import unittest
from LesserBurialChamber import LesserBurialChamber # type: ignore

class LesserBurialChamberTest(unittest.TestCase):

    def test_LesserBurialChamber(self):
        cls = LesserBurialChamber(player, roomStates)
        self.assertTrue(cls(player, roomStates["LesserBurialChamber"]["battleWon"]), "should be true")

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
    LesserBurialChamber(player, roomStates)
    unittest.main()