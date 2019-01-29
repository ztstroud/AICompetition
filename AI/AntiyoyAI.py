import level

class AntiyoyAI:
    def __init__(self, id):
        """Constructs a new AI with the given player ID."""
        
        self.id = id
    
    def getName(self):
        """Gets the displayed name of this AI."""
        
        return "Antiyoy AI"
    
    def getMoves(self, level):
        """Retrives a list of moves that the AI wants to take, given the current
        state of the level."""
        
        return []