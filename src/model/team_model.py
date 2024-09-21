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

    def increment_score(self, points=1):
        """
        Increment the team's score by a given number of points (default is 1).
        
        :param points: Number of points to add to the score
        """
        self.score += points

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
