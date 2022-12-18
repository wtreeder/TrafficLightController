import pygame

from .constants import *


class Vehicle:
    def __init__(self, vehicle_type: VehicleType, direction: Direction, lane: Lane,
                 turn: Turn):
        self.vehicle_type = vehicle_type
        self.direction = direction
        self.lane = lane
        self.turn = turn

        self.x = x_vehicle[direction.value][lane.value]
        self.y = y_vehicle[direction.value][lane.value]
        self.angle = rotation[direction.value]
        self.speed = speeds[vehicle_type.value]
        self.stop = default_stop[direction.value]

        self.is_stopped = False
        self.is_through = False
        self.is_turned = False
        self.wait_time = 0

        path = '../images/' + str(vehicle_type.value) + '.png'
        image = pygame.image.load(path)
        self.image = pygame.transform.rotate(image, self.angle)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        if direction == Direction.EAST:
            self.x -= self.width + stoppingGap
        elif direction == Direction.SOUTH:
            self.y -= self.height + stoppingGap
        elif direction == Direction.WEST:
            self.x += stoppingGap
        elif direction == Direction.NORTH:
            self.y += stoppingGap
