from enum import Enum

class Direction(Enum):
    """Defines the basic directions of movement in a hexagonal grid."""

    NORTH = 1
    NORTHEAST = 2
    SOUTHEAST = 3
    SOUTH = 4
    SOUTHWEST = 5
    NORTHWEST = 6

class UnitType(Enum):
    """Defines the types of units that exist in the game."""

    NONE = 0

    PEASANT = 1
    SPEARMAN = 2
    KNIGHT = 3
    BARON = 4

    CAPITAL = 5
    FARM = 6
    TOWER = 7
    MAGICTOWER = 8
    
    PINE = 9
    PALM = 10
    GRAVE = 11

class Unit:
    def __init__(self, type, canMove=True):
        """Constructs a new Unit with the given parameters."""
        
        self.type = type
        self.canMove = canMove
       
    @staticmethod
    def fromString(string):
        """Creates a new Unit from a string.
        
        The following strings are accepted:
        
            '-' : none
            'P' : movable peasant
            'p' : immovable pesant
            'S' : movable spearman
            's' : immovable spearman
            'K' : movable knight
            'k' : immovable knight
            'B' : movable baron
            'b' : immovable baron
            '@' : capital city
            '#' : farm
            '|' : tower
            '$' : magic tower
            '^' : pine tree
            '~' : palm tree
            'n' : grave
        
        All other strings will result in an exception."""
        
        if string == "-":
            return Unit(UnitType.NONE)
        elif string == "P":
            return Unit(UnitType.PEASANT)
        elif string == "p":
            return Unit(UnitType.PEASANT, False)
        elif string == "S":
            return Unit(UnitType.SPEARMAN)
        elif string == "s":
            return Unit(UnitType.SPEARMAN, False)
        elif string == "K":
            return Unit(UnitType.KNIGHT)
        elif string == "k":
            return Unit(UnitType.KNIGHT, False)
        elif string == "B":
            return Unit(UnitType.BARON)
        elif string == "b":
            return Unit(UnitType.BARON, False)
        elif string == "@":
            return Unit(UnitType.CAPITAL)
        elif string == "#":
            return Unit(UnitType.FARM)
        elif string == "|":
            return Unit(UnitType.TOWER)
        elif string == "$":
            return Unit(UnitType.MAGICTOWER)
        elif string == "^":
            return Unit(UnitType.PINE)
        elif string == "~":
            return Unit(UnitType.PALM)
        elif string == "t":
            return Unit(UnitType.GRAVE)
        else:
            raise Exception("Invalid unit string '%s'" % string)
       
    def toString(self):
        """Creates a string representation of this unit.
        
        The following table contains possible return values:
        
            '-' : none
            'P' : movable peasant
            'p' : immovable pesant
            'S' : movable spearman
            's' : immovable spearman
            'K' : movable knight
            'k' : immovable knight
            'B' : movable baron
            'b' : immovable baron
            '@' : capital city
            '#' : farm
            '|' : tower
            '$' : magic tower
            '^' : pine tree
            '~' : palm tree
            'n' : grave"""
        
        if self.type == UnitType.NONE:
            return "-"
        elif self.type == UnitType.PEASANT:
            return "P" if self.canMove else "p"
        elif self.type == UnitType.SPEARMAN:
            return "S" if self.canMove else "s"
        elif self.type == UnitType.KNIGHT:
            return "K" if self.canMove else "k"
        elif self.type == UnitType.BARON:
            return "B" if self.canMove else "b"
        elif self.type == UnitType.CAPITAL:
            return "@"
        elif self.type == UnitType.FARM:
            return "#"
        elif self.type == UnitType.TOWER:
            return "|"
        elif self.type == UnitType.MAGICTOWER:
            return "$"
        elif self.type == UnitType.PINE:
            return "^"
        elif self.type == UnitType.PALM:
            return "~"
        elif self.type == UnitType.GRAVE:
            return "t"
        else:
            return "?"
    
    def clone(self):
        """Creates a deep copy of this unit"""
        
        return Unit(self.type, self.canMove)
    
class Tile:
    """Represents a single tile in the level.
    
    A tile can either be water or land. If the tile is water, its owner will be
    a negative integer. If the tile is land, its owner will either be 0 (unowned)
    or a positive integer (the owner id).
    
    Land tiles can have a unit on them. See Unit for more details."""

    def __init__(self, owner, unit):
        """Constructs a new tile with the given owner and unit."""
        self.owner = owner
        self.unit = unit
    
    @staticmethod
    def fromString(string):
        """Creates a new tile from a string.

        The first character in the string represents the owner of the tile,
        as detailed in the following table:
        
                   '.' : water
                   '-' : unowned
            number 1-9 : owner id
            
        The second character in the string represents the unit present on the
        tile. See Unit.fromString for more details."""
        
        if string == "..":
            return Tile(-1, Unit(UnitType.NONE))
            
        elif string[0] == "-":
            return Tile(0, Unit.fromString(string[1]))
            
        return Tile(int(string[0]), Unit.fromString(string[1]))
    
    def toString(self):
        """Creates a string representation of this tile.
        
        The first character indicates the owner of the tile. If the tile is
        water, it will be represented by '..'.
        
        If the tile is unowned, the firt character in the string will be '-'. If
        the tile is owned, the first character in the string will be the id of
        the player that owns it. In either case, the second character in the
        string will represent the unit that is present there. See Unit.toString
        for more details."""
        
        if self.owner < 0:
            return ".."
            
        if self.owner == 0:
            return "-" + self.unit.toString()
            
        return str(self.owner) + self.unit.toString()
        
    def clone(self):
        """Creates a deep copy of this tile."""
        
        return Tile(self.owner, self.unit.clone())

class Level:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        self.tiles = []
        for y in range(height):
            self.tiles.append([])
            
            for x in range(width):
                self.tiles[y].append(Tile(0, Unit(UnitType.NONE)))

    @staticmethod
    def fromFile(filePath):
        with open(filePath, "r") as levelFile:
            width = int(levelFile.readline())
            height = int(levelFile.readline())
            
            level = Level(width, height)
            for y in range(height):
                line = levelFile.readline()
                for x in range(width):
                    if x % 2 == 0:
                        level.tiles[y][x] = Tile.fromString(line[2 * x : 2 * (x + 1)])
                        
                line = levelFile.readline()
                for x in range(width):
                    if x % 2 == 1:
                        level.tiles[y][x] = Tile.fromString(line[2 * x : 2 * (x + 1)])
                        
            return level
                        
                
    def toString(self):
        rep = ""
    
        for y in range(self.height):
            for x in range(self.width):
                if x % 2 == 0:
                    rep += self.getTile((x, y)).toString()
                else:
                    rep += "  "
            
            rep += "\n"
                
            for x in range(self.width):
                if x % 2 == 1:
                    rep += self.getTile((x, y)).toString()
                else:
                    rep += "  "
                  
            if y < self.height - 1:
                rep += "\n"
            
        return rep
        
    def clone(self):
        """Creates a deep copy of this level."""
        
        level = Level(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                level.tiles[y][x] = self.tiles[y][x].clone()
                
        return level
                
    def getTile(self, coord):
        """ Gets the tile from the given coordinate. """
        
        if self.inBounds(coord):
            return self.tiles[coord[1]][coord[0]]

        return Tile(-1, Unit(UnitType.NONE))

    def inBounds(self, coord):
        """ Determines if the given cooridnate is within the bounds of the level. """
        
        if coord[0] < 0 or coord[0] >= self.width:
            return False

        if coord[1] < 0 or coord[1] >= self.height:
            return False

        return True
    
    @staticmethod
    def getNeighbor(coord, direction):
        """ Gets the neighbor of the given tile in the given direction."""
        
        if direction == Direction.NORTH:
            return (coord[0], coord[1] - 1)

        if direction == Direction.NORTHEAST:
            if coord[0] % 2 == 0:
                return (coord[0] + 1, coord[1] - 1)
            else:
                return (coord[0] + 1, coord[1])

        if direction == Direction.SOUTHEAST:
            if coord[0] % 2 == 0:
                return (coord[0] + 1, coord[1])
            else:
                return (coord[0] + 1, coord[1] + 1)

        if direction == Direction.SOUTH:
            return (coord[0], coord[1] + 1)

        if direction == Direction.SOUTHWEST:
            if coord[0] % 2 == 0:
                return (coord[0] - 1, coord[1])
            else:
                return (coord[0] - 1, coord[1] + 1)

        if direction == Direction.NORTHWEST:
            if coord[0] % 2 == 0:
                return (coord[0] - 1, coord[1] - 1)
            else:
                return (coord[0] - 1, coord[1])
