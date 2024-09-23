import unittest
from src.model.player_model import PlayerModel

class TestPlayerModel(unittest.TestCase):

    def setUp(self):
        """Set up a sample player for testing before each test case."""
        self.player = PlayerModel("Alice Johnson", 7)

    def test_initialization(self):
        """Test that a player is initialized with correct attributes."""
        self.assertEqual(self.player.name, "Alice Johnson")
        self.assertEqual(self.player.number, 7)
        self.assertEqual(self.player.fouls, 0)
        self.assertEqual(self.player.points, 0)

    def test_commit_foul(self):
        """Test that committing a foul increments the foul count."""
        self.player.commit_foul()
        self.assertEqual(self.player.fouls, 1)

        # Test multiple fouls
        self.player.commit_foul()
        self.assertEqual(self.player.fouls, 2)

    def test_score_points(self):
        """Test that scoring points increases the player's points."""
        self.player.score_points(5)
        self.assertEqual(self.player.points, 5)

        # Test scoring additional points
        self.player.score_points(3)
        self.assertEqual(self.player.points, 8)

    def test_reset_stats(self):
        """Test that resetting stats sets fouls and points to 0."""
        # Simulate some game activity
        self.player.commit_foul()
        self.player.score_points(7)

        # Reset stats
        self.player.reset_stats()

        # Check that fouls and points are reset
        self.assertEqual(self.player.fouls, 0)
        self.assertEqual(self.player.points, 0)

if __name__ == '__main__':
    unittest.main()
