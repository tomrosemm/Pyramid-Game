import unittest
from SphinxRoom import SphinxRoom # type: ignore

class SphinxRoomTest(unittest.TestCase):

    def test_SphinxRoom(self):
        cls = SphinxRoom(player, roomStates)
        self.assertTrue(cls(player, roomStates["SphinxRoom"]["riddleSolved"]), "should be true")

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
    SphinxRoom(player, roomStates)
    unittest.main()