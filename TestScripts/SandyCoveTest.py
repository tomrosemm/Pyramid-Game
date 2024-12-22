import unittest
from SandyCove import SandyCove # type: ignore

class SandyCoveTest(unittest.TestCase):

    def test_SandyCove(self):
        cls = SandyCove(player, roomStates)
        self.assertEqual(cls(player["health"], roomStates), 100)

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
    SandyCove(player, roomStates)
    unittest.main()