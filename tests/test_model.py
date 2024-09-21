import unittest
from src.model.game_model import GameModel

class TestGameModel(unittest.TestCase):
    
    def setUp(self):
        # Set up a game model with two teams
        self.game = GameModel()

    def test_initialization(self):
        # Test that the game initializes two teams
        self.assertEqual(self.game.team1.name, "Team 1")
        self.assertEqual(self.game.team2.name, "Team 2")
        self.assertEqual(self.game.team1.score, 0)
        self.assertEqual(self.game.team2.score, 0)

    def test_increment_team1_score(self):
        # Test incrementing score for team1
        self.game.increment_team_score(1)
        self.assertEqual(self.game.team1.score, 1)

        # Test incrementing by custom points
        self.game.increment_team_score(1, 3)
        self.assertEqual(self.game.team1.score, 4)

    def test_increment_team2_score(self):
        # Test incrementing score for team2
        self.game.increment_team_score(2)
        self.assertEqual(self.game.team2.score, 1)

        # Test incrementing by custom points
        self.game.increment_team_score(2, 5)
        self.assertEqual(self.game.team2.score, 6)

if __name__ == '__main__':
    unittest.main()
