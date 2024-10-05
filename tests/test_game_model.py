import sys
import os
import time

# Add multiple directories to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src/model'))

import unittest
from game_model import GameModel

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
    
    def test_set_team_name(self):
        # Initialize the game model
        game_model = GameModel()

        # Set new team names
        game_model.set_team_name(1, "New Team 1")
        game_model.set_team_name(2, "New Team 2")

        # Verify the team names have been updated
        self.assertEqual(game_model.team1.name, "New Team 1")
        self.assertEqual(game_model.team2.name, "New Team 2")
        
    def test_start_pause_clock(self):
        game_model = GameModel()
        
        if(game_model.is_game_clock_running()):
            game_model.pause_continue_game_clock()
        
        self.assertFalse(game_model.gameClock.running)

        current_time = game_model.get_current_clock_time()
        game_model.pause_continue_game_clock()
        time.sleep(0.5)
        self.assertNotEqual(game_model.get_current_clock_time(), current_time)
        game_model.pause_continue_game_clock()
        current_time = game_model.get_current_clock_time()
        time.sleep(0.5)
        self.assertEqual(game_model.get_current_clock_time(), current_time)

if __name__ == '__main__':
    unittest.main()
