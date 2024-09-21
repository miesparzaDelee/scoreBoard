import unittest 
from src.model.game_model import GameModel 
 
class TestGameModel(unittest.TestCase): 
    def setUp(self): 
        self.game = GameModel() 
 
    def test_initial_scores(self): 
        self.assertEqual(self.game.team1_score, 0) 
        self.assertEqual(self.game.team2_score, 0) 
 
    def test_increment_team1_score(self): 
        self.game.increment_score(1) 
        self.assertEqual(self.game.team1_score, 1) 
 
if __name__ == '__main__': 
    unittest.main() 
