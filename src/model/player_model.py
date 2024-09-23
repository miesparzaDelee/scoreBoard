class PlayerModel:
    def __init__(self, name, number, fouls=0, points=0):
        """
        Initialize a player with a name, number, fouls, and points.
        
        :param name: Player's name
        :param number: Player's number
        :param fouls: Number of fouls (default 0)
        :param points: Number of points scored (default 0)
        """
        self.name = name
        self.number = number
        self.fouls = fouls
        self.points = points

    def commit_foul(self):
        """
        Add a foul to the player's record.
        """
        self.fouls += 1
        print(f"{self.name} committed a foul. Total fouls: {self.fouls}")

    def score_points(self, points):
        """
        Add points to the player's score.
        
        :param points: Number of points scored
        """
        self.points += points
        print(f"{self.name} scored {points} points. Total points: {self.points}")

    def reset_stats(self):
        """
        Reset the player's points and fouls.
        """
        self.fouls = 0
        self.points = 0
        print(f"{self.name}'s stats reset.")

# __main__ function to test PlayerModel class
if __name__ == "__main__":
    # Create a player for testing
    player = PlayerModel("Alice Johnson", 7)

    # Test foul and score methods
    player.commit_foul()
    player.score_points(5)

    # Reset stats
    player.reset_stats()
