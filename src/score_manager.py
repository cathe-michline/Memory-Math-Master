class ScoreManager:
    """Initializes the score with a starting value of 0."""
    def __init__(self):
        self.current_score = 0

    """Resets the score to 0."""
    def reset(self):
        self.current_score = 0

    """Increases the score based on how many moves the player has taken."""
    def add_match_score(self, moves_taken):
        self.current_score += max(100 - (moves_taken * 2), 10)
    
    """Returns the current score."""
    def get_score(self):
        return self.current_score
