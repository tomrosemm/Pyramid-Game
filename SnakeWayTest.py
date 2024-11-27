import unittest
from SnakeWay import SnakeWay # type: ignore

class SnakeWayTest(unittest.TestCase):

    def test_SnakeWay(self):
        cls = SnakeWay(player, roomStates)
        self.assertFalse(cls(player["hasTorch"], roomStates), "should be false")

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
    SnakeWay(player, roomStates)
    unittest.main()