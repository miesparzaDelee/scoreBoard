import unittest
from src.model.team_model import TeamModel

class TestTeamModel(unittest.TestCase):

    def test_initialization(self):
        # Test team initialization
        team = TeamModel("Eagles", description="A strong team", score=10)
        self.assertEqual(team.name, "Eagles")
        self.assertEqual(team.description, "A strong team")
        self.assertEqual(team.score, 10)
        self.assertIsNone(team.image_logo)

    def test_increment_score(self):
        # Test incrementing the team's score
        team = TeamModel("Tigers")
        team.increment_score(3)
        self.assertEqual(team.score, 3)
        
        # Test incrementing the score by default (1 point)
        team.increment_score()
        self.assertEqual(team.score, 4)

    def test_set_logo(self):
        # Test setting the team logo
        team = TeamModel("Sharks")
        team.set_logo("path/to/logo.png")
        self.assertEqual(team.image_logo, "path/to/logo.png")

    def test_set_description(self):
        # Test setting the team description
        team = TeamModel("Panthers")
        team.set_description("A fierce team")
        self.assertEqual(team.description, "A fierce team")

    def test_increment_score_through_player(self):
        # Test incrementing the score of the team when a player scores
        from src.model.player_model import PlayerModel  # Importing the PlayerModel class
        team = TeamModel("Wolves")
        
        # Create players and add them to the team
        player1 = PlayerModel("John", 10)
        player2 = PlayerModel("Sarah", 12)

        team.add_player(player1)
        team.add_player(player2)
        
        # Player scores a goal
        player1.score_points(2)
        player2.score_points(3)
        
        # Team score should be updated
        self.assertEqual(team.score, 5)

if __name__ == "__main__":
    unittest.main()
