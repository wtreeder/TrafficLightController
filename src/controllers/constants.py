from enum import Enum

x_signal = {'east': {'left': 300, 'middle': 300, 'right': 300},
            'south': {'left': 400, 'middle': 355, 'right': 305},
            'west': {'left': 490, 'middle': 490, 'right': 490},
            'north': {'left': 410, 'middle': 455, 'right': 495}}
y_signal = {'east': {'left': 410, 'middle': 455, 'right': 495},
            'south': {'left': 300, 'middle': 300, 'right': 300},
            'west': {'left': 400, 'middle': 355, 'right': 305},
            'north': {'left': 490, 'middle': 490, 'right': 490}}

x_vehicle = {'east': {'left': 0, 'middle': 0, 'right': 0},
             'south': {'left': 390, 'middle': 345, 'right': 300},
             'west': {'left': 821, 'middle': 821, 'right': 821},
             'north': {'left': 400, 'middle': 445, 'right': 490}}
y_vehicle = {'east': {'left': 400, 'middle': 445, 'right': 490},
             'south': {'left': 0, 'middle': 0, 'right': 0},
             'west': {'left': 390, 'middle': 345, 'right': 300},
             'north': {'left': 821, 'middle': 821, 'right': 821}}
speeds = {'red_car': 2.3, 'blue_car': 2.0, 'purple_car': 1.9, 'suv': 1.6, 'truck': 1.4}
stopLines = {'east': 275, 'south': 275, 'west': 545, 'north': 545}
default_stop = {'east': 270, 'south': 270, 'west': 550, 'north': 550}

left_turn_lines = {'east': 475, 'south': 475, 'west': 345, 'north': 345}
right_turn_lines = {'east': 330, 'south': 330, 'west': 490, 'north': 490}

stoppingGap = 10
movingGap = 20

rotation = {'east': 270, 'south': 180, 'west': 90, 'north': 0}


class Color(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'


class VehicleType(Enum):
    RED_CAR = 'red_car'
    BLUE_CAR = 'blue_car'
    PURPLE_CAR = 'purple_car'
    SUV = 'suv'
    TRUCK = 'truck'


class Lane(Enum):
    LEFT = 'left'
    MIDDLE = 'middle'
    RIGHT = 'right'


class Direction(Enum):
    EAST = 'east'
    SOUTH = 'south'
    WEST = 'west'
    NORTH = 'north'


class Turn(Enum):
    LEFT = 'left'
    STRAIGHT = 'straight'
    RIGHT = 'right'
