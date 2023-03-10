# Import packages
import time

import pygame

from .vehicle import Vehicle
from .constants import *


class Signal1:
    def __init__(self, left, straight, right):
        self.left = left
        self.straight = straight
        self.right = right


class State1:
    def __init__(self, east, south, west, north, stage):
        self.east = east
        self.south = south
        self.west = west
        self.north = north
        self.stage = stage


class TrafficLight1:
    # Green light states
    green1 = State1(Signal1(Color.RED, Color.GREEN, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.GREEN, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Color.GREEN)
    green2 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.GREEN, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.GREEN, Color.RED),
                    Color.GREEN)
    green3 = State1(Signal1(Color.GREEN, Color.GREEN, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.GREEN),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Color.GREEN)
    green4 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.GREEN, Color.GREEN, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.GREEN),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Color.GREEN)
    green5 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.GREEN, Color.GREEN, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.GREEN),
                    Color.GREEN)
    green6 = State1(Signal1(Color.RED, Color.RED, Color.GREEN),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.RED),
                    Signal1(Color.GREEN, Color.GREEN, Color.RED),
                    Color.GREEN)
    green7 = State1(Signal1(Color.GREEN, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.GREEN),
                    Signal1(Color.GREEN, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.GREEN),
                    Color.GREEN)
    green8 = State1(Signal1(Color.RED, Color.RED, Color.GREEN),
                    Signal1(Color.GREEN, Color.RED, Color.RED),
                    Signal1(Color.RED, Color.RED, Color.GREEN),
                    Signal1(Color.GREEN, Color.RED, Color.RED),
                    Color.GREEN)

    # Yellow light states
    yellow10 = State1(Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow13 = State1(Signal1(Color.RED, Color.GREEN, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow15 = State1(Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.GREEN, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow20 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Color.YELLOW)
    yellow24 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.GREEN, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Color.YELLOW)
    yellow26 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.GREEN, Color.RED),
                      Color.YELLOW)
    yellow30 = State1(Signal1(Color.YELLOW, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow31 = State1(Signal1(Color.YELLOW, Color.GREEN, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow37 = State1(Signal1(Color.GREEN, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.GREEN),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow40 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.YELLOW, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow42 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.YELLOW, Color.GREEN, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow48 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.GREEN, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.GREEN),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow50 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.YELLOW, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Color.YELLOW)
    yellow51 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.YELLOW, Color.GREEN, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Color.YELLOW)
    yellow57 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.GREEN, Color.YELLOW, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.GREEN),
                      Color.YELLOW)
    yellow60 = State1(Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.YELLOW, Color.YELLOW, Color.RED),
                      Color.YELLOW)
    yellow62 = State1(Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.YELLOW, Color.GREEN, Color.RED),
                      Color.YELLOW)
    yellow68 = State1(Signal1(Color.RED, Color.RED, Color.GREEN),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.RED),
                      Signal1(Color.GREEN, Color.YELLOW, Color.RED),
                      Color.YELLOW)
    yellow70 = State1(Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Color.YELLOW)
    yellow73 = State1(Signal1(Color.GREEN, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.GREEN),
                      Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Color.YELLOW)
    yellow75 = State1(Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.GREEN, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.GREEN),
                      Color.YELLOW)
    yellow80 = State1(Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow84 = State1(Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.GREEN, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.GREEN),
                      Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Color.YELLOW)
    yellow86 = State1(Signal1(Color.RED, Color.RED, Color.GREEN),
                      Signal1(Color.YELLOW, Color.RED, Color.RED),
                      Signal1(Color.RED, Color.RED, Color.YELLOW),
                      Signal1(Color.GREEN, Color.RED, Color.RED),
                      Color.YELLOW)

    # Red light states
    red0 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                  Signal1(Color.RED, Color.RED, Color.RED),
                  Signal1(Color.RED, Color.RED, Color.RED),
                  Signal1(Color.RED, Color.RED, Color.RED),
                  Color.RED)
    red13 = State1(Signal1(Color.RED, Color.GREEN, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Color.RED)
    red24 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.GREEN, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Color.RED)
    red15 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.GREEN, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Color.RED)
    red26 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.GREEN, Color.RED),
                   Color.RED)
    red37 = State1(Signal1(Color.GREEN, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.GREEN),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Color.RED)
    red48 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.GREEN, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.GREEN),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Color.RED)
    red57 = State1(Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.GREEN, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.GREEN),
                   Color.RED)
    red68 = State1(Signal1(Color.RED, Color.RED, Color.GREEN),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.RED, Color.RED, Color.RED),
                   Signal1(Color.GREEN, Color.RED, Color.RED),
                   Color.RED)

    #
    current_state = green1

    # Transitions
    def to_green(self):
        if self.current_state.stage != Color.GREEN:
            return 'error'

    # def to_yellow(self):

    # def to_red(self):


t = TrafficLight1()


# print(t.current_state.east.straight.value)


class Signal:
    def __init__(self, direction: Direction, lane: Lane, turn: bool, color: Color):
        self.direction = direction
        self.lane = lane
        self.turn = turn
        self.color = color

        self.x = x_signal[self.direction.value][self.lane.value]
        self.y = y_signal[self.direction.value][self.lane.value]

        self._load_image()

    def to_red(self):
        self.turn = False
        self.color = Color.RED
        self._load_image()

    def to_yellow(self):
        self.turn = False
        self.color = Color.YELLOW
        self._load_image()

    def to_green(self):
        self.turn = False
        self.color = Color.GREEN
        self._load_image()

    def to_right_turn_yellow(self):
        self.turn = True
        self.color = Color.YELLOW
        self._load_image()

    def to_right_turn_green(self):
        self.turn = True
        self.color = Color.GREEN
        self._load_image()

    def _load_image(self):
        if self.turn:
            path = '../images/' + str(self.lane.value) + '_turn_' + str(self.color.value) + '.png'
        else:
            path = '../images/' + str(self.lane.value) + '_' + str(self.color.value) + '.png'
        image = pygame.image.load(path)
        self.image = pygame.transform.rotate(image, rotation[self.direction.value])


class TrafficLightController:
    def __init__(self):
        for direction in Direction:
            for lane in Lane:
                self.signals[direction.value][lane.value] = Signal(direction, lane, False,
                                                                   Color.RED)

    signals = {'east': {'left': None, 'middle': None, 'right': None},
               'south': {'left': None, 'middle': None, 'right': None},
               'west': {'left': None, 'middle': None, 'right': None},
               'north': {'left': None, 'middle': None, 'right': None}}

    vehicles = {'east': {'left': [], 'middle': [], 'right': [], 'turned_left': [], 'turned_right': []},
                'south': {'left': [], 'middle': [], 'right': [], 'turned_left': [], 'turned_right': []},
                'west': {'left': [], 'middle': [], 'right': [], 'turned_left': [], 'turned_right': []},
                'north': {'left': [], 'middle': [], 'right': [], 'turned_left': [], 'turned_right': []}}

    wait_times = {'east': {'left': 0, 'straight': 0, 'right': 0},
                  'south': {'left': 0, 'straight': 0, 'right': 0},
                  'west': {'left': 0, 'straight': 0, 'right': 0},
                  'north': {'left': 0, 'straight': 0, 'right': 0}}

    # Add vehicle
    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.direction.value][vehicle.lane.value].append(vehicle)

    # Update signals
    def update_signals(self):
        self.signals[Direction.EAST.value][Lane.LEFT.value].to_green()
        self.signals[Direction.EAST.value][Lane.MIDDLE.value].to_green()
        self.signals[Direction.EAST.value][Lane.RIGHT.value].to_green()
        self.signals[Direction.SOUTH.value][Lane.RIGHT.value].to_right_turn_green()

        time.sleep(10)

        self.signals[Direction.EAST.value][Lane.LEFT.value].to_yellow()
        self.signals[Direction.SOUTH.value][Lane.RIGHT.value].to_right_turn_yellow()

        time.sleep(2)

        self.signals[Direction.EAST.value][Lane.LEFT.value].to_red()
        self.signals[Direction.SOUTH.value][Lane.RIGHT.value].to_red()

        time.sleep(1)

        self.signals[Direction.WEST.value][Lane.MIDDLE.value].to_green()
        self.signals[Direction.WEST.value][Lane.RIGHT.value].to_green()

        time.sleep(10)

        self.signals[Direction.EAST.value][Lane.MIDDLE.value].to_yellow()
        self.signals[Direction.EAST.value][Lane.RIGHT.value].to_yellow()

        time.sleep(2)

        self.signals[Direction.EAST.value][Lane.MIDDLE.value].to_red()
        self.signals[Direction.EAST.value][Lane.RIGHT.value].to_red()

        time.sleep(1)

        self.signals[Direction.WEST.value][Lane.LEFT.value].to_green()
        self.signals[Direction.NORTH.value][Lane.RIGHT.value].to_right_turn_green()

        time.sleep(10)

        self.signals[Direction.WEST.value][Lane.LEFT.value].to_yellow()
        self.signals[Direction.WEST.value][Lane.MIDDLE.value].to_yellow()
        self.signals[Direction.WEST.value][Lane.RIGHT.value].to_yellow()
        self.signals[Direction.NORTH.value][Lane.RIGHT.value].to_right_turn_yellow()

        time.sleep(2)

        self.signals[Direction.WEST.value][Lane.LEFT.value].to_red()
        self.signals[Direction.WEST.value][Lane.MIDDLE.value].to_red()
        self.signals[Direction.WEST.value][Lane.RIGHT.value].to_red()
        self.signals[Direction.NORTH.value][Lane.RIGHT.value].to_red()

        time.sleep(1)

        self.signals[Direction.SOUTH.value][Lane.LEFT.value].to_green()
        self.signals[Direction.SOUTH.value][Lane.MIDDLE.value].to_green()
        self.signals[Direction.SOUTH.value][Lane.RIGHT.value].to_green()
        self.signals[Direction.WEST.value][Lane.RIGHT.value].to_right_turn_green()

        time.sleep(10)

        self.signals[Direction.SOUTH.value][Lane.LEFT.value].to_yellow()
        self.signals[Direction.WEST.value][Lane.RIGHT.value].to_right_turn_yellow()

        time.sleep(2)

        self.signals[Direction.SOUTH.value][Lane.LEFT.value].to_red()
        self.signals[Direction.WEST.value][Lane.RIGHT.value].to_red()

        time.sleep(1)

        self.signals[Direction.NORTH.value][Lane.MIDDLE.value].to_green()
        self.signals[Direction.NORTH.value][Lane.RIGHT.value].to_green()

        time.sleep(10)

        self.signals[Direction.SOUTH.value][Lane.MIDDLE.value].to_yellow()
        self.signals[Direction.SOUTH.value][Lane.RIGHT.value].to_yellow()

        time.sleep(2)

        self.signals[Direction.SOUTH.value][Lane.MIDDLE.value].to_red()
        self.signals[Direction.SOUTH.value][Lane.RIGHT.value].to_red()

        time.sleep(1)

        self.signals[Direction.NORTH.value][Lane.LEFT.value].to_green()
        self.signals[Direction.EAST.value][Lane.RIGHT.value].to_right_turn_green()

        time.sleep(10)

        self.signals[Direction.NORTH.value][Lane.LEFT.value].to_yellow()
        self.signals[Direction.NORTH.value][Lane.MIDDLE.value].to_yellow()
        self.signals[Direction.NORTH.value][Lane.RIGHT.value].to_yellow()
        self.signals[Direction.EAST.value][Lane.RIGHT.value].to_right_turn_yellow()

        time.sleep(2)

        self.signals[Direction.NORTH.value][Lane.LEFT.value].to_red()
        self.signals[Direction.NORTH.value][Lane.MIDDLE.value].to_red()
        self.signals[Direction.NORTH.value][Lane.RIGHT.value].to_red()
        self.signals[Direction.EAST.value][Lane.RIGHT.value].to_red()

        time.sleep(1)



    # Update vehicles
    def update_vehicles(self):
        for direction in self.vehicles:
            for lane in self.vehicles[direction]:
                for vehicle in self.vehicles[direction][lane]:
                    index = self.vehicles[direction][lane].index(vehicle)
                    front_vehicle = None
                    if len(self.vehicles[direction][lane]) > 1 and index > 0:
                        front_vehicle = self.vehicles[direction][lane][self.vehicles[direction][lane].index(vehicle) - 1]

                    self._is_through(vehicle)
                    self._stop(vehicle, front_vehicle)
                    self._move(vehicle, front_vehicle, index)

    def _is_through(self, v: Vehicle):
        if v.direction == Direction.EAST:
            if not v.is_through and v.x + v.width > stopLines[v.direction.value]:
                v.is_through = True
        elif v.direction == Direction.SOUTH:
            if not v.is_through and v.y + v.height > stopLines[v.direction.value]:
                v.is_through = True
        elif v.direction == Direction.WEST:
            if not v.is_through and v.x < stopLines[v.direction.value]:
                v.is_through = True
        elif v.direction == Direction.NORTH:
            if not v.is_through and v.y < stopLines[v.direction.value]:
                v.is_through = True

    def _stop(self, v: Vehicle, front: Vehicle):
        if front is not None and not front.is_through:
            if v.direction == Direction.EAST:
                v.stop = front.stop - front.width - stoppingGap
            elif v.direction == Direction.SOUTH:
                v.stop = front.stop - front.height - stoppingGap
            elif v.direction == Direction.WEST:
                v.stop = front.stop + front.width + stoppingGap
            elif v.direction == Direction.NORTH:
                v.stop = front.stop + front.height + stoppingGap

    def _move(self, v: Vehicle, front: Vehicle, index: int):
        if v.direction == Direction.EAST:
            if (v.x + v.width <= v.stop
                or v.is_through
                or (self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and not self.signals[v.direction.value][v.lane.value].turn)
                or (v.turn == Turn.RIGHT
                    and self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and self.signals[v.direction.value][v.lane.value].turn)) \
                    and (index == 0
                         or v.x + v.width < front.x - stoppingGap):
                if v.turn == Turn.LEFT and v.x + v.width >= left_turn_lines[v.direction.value]:
                    self.vehicles[Direction.NORTH.value]['turned_left'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.NORTH
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 90)
                    v.x = v.x + v.width - v.height
                    v.y = v.y - v.width + v.height
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                elif v.turn == Turn.RIGHT and v.x + v.width >= right_turn_lines[v.direction.value]:
                    self.vehicles[Direction.SOUTH.value]['turned_right'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.SOUTH
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 270)
                    v.x = v.x + v.width - v.height
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                else:
                    v.x += v.speed
            else: v.is_stopped = True
        elif v.direction == Direction.SOUTH:
            if (v.y + v.height <= v.stop
                or v.is_through
                or (self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and not self.signals[v.direction.value][v.lane.value].turn)
                or (v.turn == Turn.RIGHT
                    and self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and self.signals[v.direction.value][v.lane.value].turn)) \
                    and (index == 0
                         or v.y + v.height < front.y - stoppingGap):
                if v.turn == Turn.LEFT and v.y + v.height >= left_turn_lines[v.direction.value]:
                    self.vehicles[Direction.EAST.value]['turned_left'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.EAST
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 90)
                    v.y = v.y - v.width + v.height
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                elif v.turn == Turn.RIGHT and v.y + v.height >= right_turn_lines[v.direction.value]:
                    self.vehicles[Direction.WEST.value]['turned_right'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.WEST
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 270)
                    v.x = v.x + v.width - v.height
                    v.y = v.y - v.width + v.height
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                else:
                    v.y += v.speed
            else: v.is_stopped = True
        elif v.direction == Direction.WEST:
            if (v.x >= v.stop
                or v.is_through
                or (self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and not self.signals[v.direction.value][v.lane.value].turn)
                or (v.turn == Turn.RIGHT
                    and self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and self.signals[v.direction.value][v.lane.value].turn)) \
                    and (index == 0
                         or v.x > front.x + front.width + stoppingGap):
                if v.turn == Turn.LEFT and v.x <= left_turn_lines[v.direction.value]:
                    self.vehicles[Direction.SOUTH.value]['turned_left'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.SOUTH
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 90)
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                elif v.turn == Turn.RIGHT and v.x <= right_turn_lines[v.direction.value]:
                    self.vehicles[Direction.NORTH.value]['turned_right'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.NORTH
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 270)
                    v.y = v.y - v.width + v.height
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                else:
                    v.x -= v.speed
            else: v.is_stopped = True
        elif v.direction == Direction.NORTH:
            if (v.y >= v.stop
                or v.is_through
                or (self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and not self.signals[v.direction.value][v.lane.value].turn)
                or (v.turn == Turn.RIGHT
                    and self.signals[v.direction.value][v.lane.value].color == Color.GREEN
                    and self.signals[v.direction.value][v.lane.value].turn)) \
                    and (index == 0
                         or v.y > front.y + front.height + stoppingGap):
                if v.turn == Turn.LEFT and v.y <= left_turn_lines[v.direction.value]:
                    self.vehicles[Direction.WEST.value]['turned_left'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.WEST
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 90)
                    v.x = v.x + v.width - v.height
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                elif v.turn == Turn.RIGHT and v.y <= right_turn_lines[v.direction.value]:
                    self.vehicles[Direction.EAST.value]['turned_right'].append(v)
                    del self.vehicles[v.direction.value][v.lane.value][index]
                    v.is_turned = True
                    v.direction = Direction.EAST
                    v.turn = Turn.STRAIGHT
                    v.image = pygame.transform.rotate(v.image, 270)
                    v.width = v.image.get_width()
                    v.height = v.image.get_height()
                else:
                    v.y -= v.speed
            else: v.is_stopped = True

