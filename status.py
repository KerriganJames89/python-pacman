from enum import Enum

class Direction(Enum):
  Left  = 0
  Up    = 1
  Right = 2
  Down  = 3

class Axis(Enum):
  Horizontal = 0
  Vertical = 1

class ghost_mode(Enum):
  chase = 0
  scatter = 1
  frightened = 2
  eaten = 3

class corner(Enum):
  top_right = 0
  top_left = 1
  bottom_right = 2
  bottom_left = 3