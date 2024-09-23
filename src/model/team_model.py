class TeamModel:
    def __init__(self, name, image_logo=None, description="", score=0):
        """
        Initialize a team with a name, optional image logo, description, and score.
        
        :param name: The team's name
        :param image_logo: Path to the team's logo image (optional)
        :param description: A brief description of the team
        :param score: The team's score (default 0)
        """
        self.name = name
        self.image_logo = image_logo
        self.description = description
        self.score = score
        self.players = []

    def increment_score(self, points=1):
        """
        Increment the team's score by a given number of points (default is 1).
        
        :param points: Number of points to add to the score
        """
        self.score += points
        print(f"Team {self.name} score incremented by {points}. Total score: {self.score}")

    def set_logo(self, image_path):
        """
        Set the team's logo image.
        
        :param image_path: Path to the logo image
        """
        self.image_logo = image_path

    def set_description(self, description):
        """
        Set a brief description of the team.
        
        :param description: Team's description
        """
        self.description = description

    def add_player(self, player):
        """
        Add a player to the team.
        
        :param player: PlayerModel object
        """
        self.players.append(player)
        player.set_currentTeam(self)

    def player_score(self, player_number, points):
        """
        Handle scoring for a player and update the team score.
        
        :param player_number: The number of the player who scored
        :param points: The points scored
        """
        player = self.get_player_by_number(player_number)
        if player:
            player.score_points(points)
            self.increment_score(points)
        else:
            print(f"Player with number {player_number} not found in team {self.name}.")

    def get_player_by_number(self, player_number):
        """
        Get a player by their number.
        
        :param player_number: The player's number
        :return: The PlayerModel object if found, otherwise None
        """
        for player in self.players:
            if player.number == player_number:
                return player
        return None

    def team_summary(self):
        """
        Print a summary of the team and its players.
        """
        print(f"Team: {self.name}, Score: {self.score}")
        print(f"Description: {self.description}")
        print(f"Logo: {self.image_logo}")
        for player in self.players:
            print(f"Player {player.name}, Number: {player.number}, Points: {player.points}, Fouls: {player.fouls}")
        print(f"Team Points: {self.score}")

# __main__ function to test TeamModel class
if __name__ == "__main__":
    from player_model import PlayerModel  # Import PlayerModel for testing

    # Create a team for testing
    team = TeamModel("Eagles")

    # Create players and add them to the team
    player1 = PlayerModel("Alice Johnson", 7)
    player2 = PlayerModel("Bob Smith", 10)
    team.add_player(player1)
    team.add_player(player2)

    # Test scoring and team update
    team.player_score(7, 5)  # Alice scores 5 points
    team.player_score(10, 3)  # Bob scores 3 points

    # Print team summary
    team.team_summary()
